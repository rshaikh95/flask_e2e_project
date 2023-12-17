# flask_e2e_project

For this final project, I will combine many of the tools and services explored over the semester.

A combination of the tools and services we learned this semester.

This is a simple Flask app that shows patient ID and their MRN values. The app shows patients ID and their MRN obtained from MySQL database which is connected via Azure. Dataset using a TABLE from a DATABASE in MySQL showed here in HTML. The values are randomly generated using Faker. 

For this app, I have used Github, Flask (Python; Frotend & Backend), MySQL (Database via Azure), SQLAlchemy (ORM), .ENV (Environment Variables), Tailwind (Frontend Styling), Authorization (Google OAuth), API Service (Flask Backend), Sentry.io (Debugging & Logging) ,Docker (Containerization) and Azure (Deployment).

You can run this web service locally via command python app.py.

Through docker using  docker run -d -p 5001:5000 shaikh located in the Dockerfile.

Or through the cloud using azure web app with the link: rahilwebapp.azurewebsites.net

The App Home Page looks like this when deployed

![App Home Page1](https://github.com/rshaikh95/flask_e2e_project/assets/141374132/de83fde5-7d79-485f-9647-f855e946ec4a)

The data page displays the patients ID and their MRN obtained from MySQL database which is connected via Azure

![Data Page](https://github.com/rshaikh95/flask_e2e_project/assets/141374132/23e3208a-3e9c-4f1a-a7e5-f799cd2ff382)

The EER diagram obtained from MySQL shows the tables and values used

![EER Diagram](https://github.com/rshaikh95/flask_e2e_project/assets/141374132/9de1ff5b-4139-4d62-bae3-3e0a501724bc)

The sentry log showing logs and errors is displayed here

![Sentry log](https://github.com/rshaikh95/flask_e2e_project/assets/141374132/5e180400-d6cf-4a2b-8ede-080276d59bbd)

