import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
from flask import Flask, render_template, url_for, redirect, session
import sentry_sdk
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from db_functions import update_or_create_user
import pymysql

sentry_sdk.init(
    dsn="https://58707ec0c5fe8bb72714b78d07083872@o4506404419338240.ingest.sentry.io/4506404437688320",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

load_dotenv()  # Load environment variables from .env file

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

# Example usage
tables = get_tables(db_engine)
sql_query = "SELECT * FROM patients"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://8080-cs-619443806516-default.cs-us-east1-rtep.cloudshell.dev//google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])
## create a route that throws an error

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

@app.route('/data')
def data(data=df):

    print("Tables in the database:", tables)
    print(df)
    data = data.sample(15)
    return render_template('data.html', data=data)

## create a db connection error 
@app.route('/db-error')
def db_error():
    conn = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}')
    try:
        conn.connect()
    except Exception as e:
        raise Exception(f'Error connecting to the database: {e}')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')   

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )