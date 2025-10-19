# Django Notes

Django is a web framework to generate HTML and CSS for dynamic web applications.

### Quick Guide: Step-by-Step

Everything creating a new app, say `newApp`, follow these steps:
1. Go to `settings.py` of project, add the new app to `INSTALLED_APP` list.
2. Go to `urls.py` of project, add new path like `path('newApp/', include("newApp.urls"))` in `urlpatterns` list.
3. Go to the `newApp/` directory, create a new file called `urls.py`.
4. Open `urls.py` and add the following:
```
from django.urls import path
from . import views

app_name = "newApp"             <--- Uniquely identify this app to avoid name confusion
urlpatterns = [
    path("", views.index, name="index")
]
```
5. Now, we can write this `index` function in `views.py` of newApp. 
6. Go to `newApp/` directory, create a new folder called `templates/` then another new folder called `tasks/`.
7. Inside `newApp/templates/tasks` directory, create a new file called `index.html`.
8. Now we can write HTML in `index.html`.

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

### New Year's App: Conditional and Static Files (Styling)

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
|   |-- static/             <--- Static files
|   |   |-- newyear/
|   |       |-- styles.css
|   |-- templates/
|   |   |-- newyear/
|   |       |-- index.html
```
```
// newyear > templates > newyear > index.html

{% load static %}   <--- Django will figure out where the static files are

<!doctype html>
<html lang="en">
    <head>
        <title>Is it New Year's?</title>
        <link href="{% static 'newyear/styles.css' %}" rel="stylesheet">
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
## Tasks and Form

Try the `tasks` todo app using `{% for lop %}`.

```
// tasks/views.py

from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
```
```
// tasks/views.py

tasks = [
    "Drink more coffee",
    "Exercise 2 times a week",
    "Go to swim"
]

// redner task in tasks in index.html
def index(request):
    return render(request, "tasks/index.html". {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")
```
```
// tasks/templates/tasks/index.html

<!doctype html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <ul>
            {% for task in tasks%}
                <li>{{task}}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```
```
// tasks/templates/tasks/add.html

<!doctype html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <h1>Add Task</h1>
        <form>
            <input type="text" name="task">
            <input type="submit">
        </form>
    </body>
</html>
```
## Template Inheritance

Create `layout.html` in `tasks/templates/tasks/`. use `{% block %}` to tell Django that we will be using the same layout, but inside the body, the content inside the `block` will change, depending on which `.html` we're using.
```
//layout.html
<!doctype html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        {% block body%}
        {% endblock%}
    </body>
</html>
```
Now, inside `index.html` and `add.html`:

```
// index.html

{% extends "tasks/layout.html %}

{% block body %}
    <ul>
        {% for task in tasks%}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'tasks: add' %}">Add a New Task</a>         <--- Link this 'Add a New Task' to add.html by referring to name='add' in urls.py of "tasks" app
{% endblock %}
```
```
// add.html

{% extends "tasks/layout.html %}

{% block body %}
    <h1>Add Task</h1>
    <form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks: index' %}">View Tasks</a>
{% endblock %}
```
### Use the Built-In Form in Django & Sessions

Sessions remembers the user and stores user data. To use session:
- We need to run `python manage.py migrate` to create the table for storing user data.

```
// tasks/views.py

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

// Get rid of global variable and use session
<!-- tasks = [
    "Drink more coffee",
    "Exercise 2 times a week",
    "Go to swim"
] -->

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

// render task in tasks in index.html
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []               <--- Add session
    return render(request, "tasks/index.html". {
        "tasks": request.session["tasks"]           <--- Add session
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
            if form.is_valid():                      <--- Check if user provides the data correctly or in the right format
                task = form.cleaned_data["task"]     <--- If the form is valud, we take the data from the form, get the "task"
                request.session["task] += [tasks]    <--- Add "task" to tasks list using session
                return HttpResponseRedirect(reverse("tasks: index"))     <--- Redirect user back to index.html
            else:
                return render(request, "tasks/add.html", {
                    "form": form                    <--- If not valid, render the same add.html back to user
                })

    return render(request, "tasks/add.html", {
        "form": newTaskForm()                       <--- Create a blank form with two fields: New Task and Priority
    })
```
```
// add.html

{% extends "tasks/layout.html %}

{% block body %}
    <h1>Add Task</h1>
    <form action="{% url 'tasks: add' %}" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
    <a href="{% url 'tasks: index' %}">View Tasks</a>
{% endblock %}
```
```
// index.html

{% extends "tasks/layout.html %}

{% block body %}
    <ul>
        {% for task in tasks%}
            <li>{{ task }}</li>
        {% empty %}
            <li>No tasks.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'tasks: add' %}">Add a New Task</a>
{% endblock %}
```

### Django REST Framework

**Models**: Define how data is structured.
**Serializer**: To convert python object to JSON in communication, i.e., API.
**View**: Import **models**. Like sending an HTTP request. A view function must have a request variable, i.e., `def createUser(request)`.
**urls**: Import **views**.

Watch video: [CS50W - Lecture 3 - Django](https://www.youtube.com/watch?v=w8q0C-C1js4)
Read more: [freeCodeCamp - Django](https://www.freecodecamp.org/news/tag/django/)
[Django Tutorial](https://studygyaan.com/cheatsheet/django)