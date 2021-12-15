![](https://i.ibb.co/ZS81sWQ/logo.png[/img][/url])

# ParkingWeb/Authorization

- This is a microservice, as REST API, using DjangoRestFramework and PostgreSQL. 
- Backend for a customer, admin user authentication, and register in the application. 

## Setup

The first thing to do is to clone the repository:
```bash
git clone https://github.com/g2p17/backend_parking.git
cd backend_parking
```
Create a virtual environment to install dependencies in and activate it:
```bash
python -m venv env
env\Scripts\activate
```

## Installation
Then install the dependencies:
```bash
(env) python -m pip install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

## Usage
Once pip has finished downloading the dependencies:
```bash
(env) python manage.py makemigrations
(env) python manage.py migrate
(env) python manage.py runserver
```
And navigate to http://127.0.0.1:8000

## API Documentation
In [http://127.0.0.1:8000/swagger/]() you can find all operations, models and data

![](https://i.ibb.co/0B4XxSL/Swagger-MSParking-Lot.jpg])

## Credits
**Github:@juan13ut, Github:@toyaVaroa**  and **Github:@daorjuelah** collaborate in this project and we appreciate the supervision of **Github:@casierrav**


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
