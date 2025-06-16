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
|   |-- urls.py             <-- Create this for myApp
|   |-- views.py            <-- Each view is like something that user wants to see, i.e., user makes a request, you process, then send back the response.
|-- lecture3/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py             <-- Table of contents. This is for the entire project.
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
```

- **`python manage.py runserver`**: Run the web server.
- **`python manage.py createsuperuse`**: Create superuser. Will prompt username and password, to access `admin`.

## Routes
Open `settings.py` and add `myApp` to `INSTALLED_APPS`.
Generally, need to import functions.

```
// views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def brian(request):
    return HttpResponse("Hi Brian.")

def david(request):
    return HttpResponse("Hi David.")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
```
```
// myApp > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index),
    path("brian", views.brian, name="brian"),
    path("brian", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")
]
```
Now, go to the `lecture3` and open `urls.py`, then add the `myApp` that newly created and import `include`:
```
// lecture3 > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myApp/", include(myApp.urls))
]
```
Now, when we `runserver` and type `127.0.0.1:8000/myApp/`, we will see "Hello world!". <br>
If we type `127.0.0.1:8000/myApp/brian`, we will see "Hello Brian." <br>
If we type `127.0.0.1:8000/myApp/lucy`, we will see "Hello, Lucy!."

## Templates

Instead of speciying each url, we can use create an `index.html` for each page:
```
// myApp > views.py
def index(request):
    return render(request, "myApp/index.html")
```
```
lecture3/
|-- myApp/
|   |-- migrations/
|   |-- templates/
|   |   |-- hello/          <-- Create this template called 'hello' and index.html
|   |       |-- index.html
```
```
// myApp > templates > hello > index.html
<!doctype html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h5>Hello, worldddd!</h5>
    </body>
</html>
```
Now, when type `127.0.0.1:8000/hello/`, we will see <h5>Hello, worldddd!</h5>





Watch video: [CS50W - Lecture 3 - Django](https://www.youtube.com/watch?v=w8q0C-C1js4)