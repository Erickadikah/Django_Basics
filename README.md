# Django Basics

## Django Installation

### Install Git

- Download and install Git from [here](https://git-scm.com/downloads)
- Open command prompt and type `git --version` to check if Git is installed correctly

### Install VS Code

- Download and install VS Code from [here](https://code.visualstudio.com/download)

### Install VS Code Extensions

- Open VS Code and install the following extensions
  - Python
  - Django
  - Django Template
  - Django Snippets
  - Django AutoComplete
  - Django Model Snippets
  - Django Template Snippets
  - Django Template Highlighter
  - Django HTML
  - Django HTML Snippets
  - Django Template Language Support
  - Django Template Tag
  - Django Template Tag Wrapper
  - Django Template Tag Completion
  - Django Template Tag Bundle
  - Django Template Tag Helper
    - Django Snippets
    - Django Template Snippets
    - Django Model Snippets
    - Django Template Highlighter
    - Django HTML
    - Django HTML Snippets
    - Django Template Language Support
    - Django Template Tag
    - Django Template Tag Wrapper
    - Django Template Tag Completion
    - Django Template Tag Bundle


### Install Python

- Download and install Python 3.7.4 from [here](https://www.python.org/downloads/release/python-374/)
- Add Python to PATH
- Open command prompt and type `python --version` to check if Python is installed correctly

### Install Django

- Open command prompt and type `pip install django` to install Django
- Type `django-admin --version` to check if Django is installed correctly

## Create a Django Project

- Open command prompt and type `django-admin startproject <project_name>` to create a Django project


## Create a Django App

- Open command prompt and type `cd <project_name>` to go to the project directory
- Type `python manage.py startapp <app_name>` to create a Django app

## Run the Django Server

- Open command prompt and type `python manage.py runserver` to run the Django server

## Create a Superuser

- Open command prompt and type `python manage.py createsuperuser` to create a superuser

## Create a Django Model

- Open `models.py` file in the app directory
- Create a class that inherits from `models.Model`

```python

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False) # null=True, default=True
```

# Running in a Virtual Environment

## Create a Virtual Environment

- Open command prompt and type `python -m venv <venv_name>` to create a virtual environment

## Activate a Virtual Environment

- Open command prompt and type `<venv_name>\Scripts\activate` to activate the virtual environment

## Deactivate a Virtual Environment

- Open command prompt and type `deactivate` to deactivate the virtual environment

## Install Django in a Virtual Environment

- Open command prompt and type `pip install django` to install Django in the virtual environment
s
