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

Instead of specifying each url, we can use create an `index.html` for each page:
```
// myApp > views.py

def index(request):
    return render(request, "myApp/index.html")

def greet(request, name):
    return render(request, "myApp/greet.html", {
        "name": name.capitalize()
    })
```
```
lecture3/
|-- myApp/
|   |-- migrations/
|   |-- templates/
|   |   |-- hello/          <-- Create this template called 'hello' and index.html
|   |       |-- index.html
|   |       |-- greet.html
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

// myApp > templates > hello > greet.html

<!doctype html>
<html lang="en">
    <head>
        <title>Hello</title>
    </head>
    <body>
        <p>Hello, {{name}}!</p>   <--- Use double curly braces, a Django script.
    </body>
</html>
```
Now, when type `127.0.0.1:8000/hello/`, we will see <h5>Hello, worldddd!</h5>
When we render the `127.0.0.1:8000/hello/ron` page, we will see `Hello, Ron!`.

Try the `newyear` app, if today is the New Year's day, using Django conditional statements with `{% %}`.

```
// newyear > views.py

from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```
```
lecture3/
|-- newyear/
|   |-- migrations/
|   |-- templates/
|   |   |-- newyear/
|   |       |-- index.html
```
```
// newyear > templates > newyear > index.html

<!doctype html>
<html lang="en">
    <head>
        <title>Is it New Year's?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

Watch video: [CS50W - Lecture 3 - Django](https://www.youtube.com/watch?v=w8q0C-C1js4)