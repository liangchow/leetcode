# Django Notes

Django is a web framework to generate HTML and CSS for dynamic web applications.

## Set-Up
If using VS Code, install these extensions: `Python` and `SQLite Viewer`.

Next, install:
- **`pip install pipenv`**: Virtual environment.
- **`pipenv install django`**: Use `pipenv` to install `django`. 

After the installation:
- **`pipenv shell`**: Launch virtual environment.
- **`django-admin startproject lecture3 `**: Create a project called `lecture3` with some starter files. We can use `python manage.py <command>` or `django-admin` interchangely.
- **`python manage.py startapp myApp`**: Create an app called `myApp`.
```
lecture3/
|-- myApp/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py    <---- Each view is like something that user wants to see, i.e., user makes a request, you process, then send back the response.
|-- lecture3/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py      <---- Table of contents
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
```

- **`python manage.py runserver`**: Run the web server.
- **`python manage.py createsuperuse`**: Create superuser. Will prompt username and password, to access `admin`.

## Settings.py and Views.py
Open `settings.py` and add `myApp` to `INSTALLED_APPS`.

```
// views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

```



Watch video: [CS50W - Lecture 3 - Django](https://www.youtube.com/watch?v=w8q0C-C1js4)