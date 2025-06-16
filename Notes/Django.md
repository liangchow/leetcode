# Django Notes

## Set-Up
If using VS Code, install these extensions: `Python` and `SQLite Viewer`.

Next, install:
- **`pip install pipenv`**: Virtual environment.
- **`pipenv install django`**: Use `pipenv` to install `django`. 

After the installation:
- **`pipenv shell`**: Launch virtual environment.
- **`django-admin startproject firstproject `**: Create a project called `firstproject`. We can use `python manage.py <command>` or `django-admin` interchangely.
- **`python manage.py startapp firstapp`**: Create an app called `firstapp`.
```
firstproject/
|-- firstapp/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- manage.py
```
## Views.py
`View` is where we take user request, process them and send back with response. In other words, `view` deals with logic parts of the application.
Open `views.py` and change the interpreter to the one virtual environment version (`pipenv`) to resolve the errors.


## Built-In Components
- **`python manage.py createsuperuse`**: Create superuser. Will prompt username and password, to access `admin`.
