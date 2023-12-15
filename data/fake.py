from flask import Flask, render_template
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker
from sqlalchemy import text

#Used this app first to create fake data, data inserted but app doesn't work don't run, run app.py directly
    # Load environment variables
    load_dotenv()

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
    fake = Faker(locale="en_US")

    def insert_fake_data(engine, num_records=100):
        # Start a connection
        with engine.connect() as connection:
            # Insert fake data into patients
            for _ in range(num_records):
                MRN = fake.unique.random_number(digits=10)
                connection.execute(f"INSERT INTO patients (MRN) VALUES ('{MRN}')")
            
            # Fetch all patient IDs
            patient_ids = [row[0] for row in connection.execute("SELECT patient_id FROM patients").fetchall()] # Noqa: E501
            
           

    if __name__ == "__main__":
        insert_fake_data(db_engine)
        print("Fake data insertion complete!")

        


