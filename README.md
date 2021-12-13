# Fleet Vehicle API

## Simple REST API builds with Django-rest-framework
API for accounting of drivers and fleet vehicles.

- Displaying a list of drivers
- Shows a list of drivers filtered by date
- Displaying driver information
- CRUD driver
- Displaying a list of vehicles
- Display of vehicles filtered by the presence of a driver
- Displaying information for a specific vehicle
- CRUD vehicle
- Removing, changing the driver in the vehicle

## Running locally:

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

3 - Run app:

`python3 manage.py runserver`
