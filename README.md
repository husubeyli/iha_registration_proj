{% if False %}

# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 

Template is written with django 1.11 and python 3 in mind.


### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Deployment AWS ubuntu 

* Separated requirements files

* PostgresSQL by default if no env variable is set

# Usage

To use this template to start your own project:

### Existing virtualenv

First create virtual envoirment
python -m venv .venv

Then activate
source .venv/bin/activate

Requirements file 
$ pip install -r requirements.txt

### No virtualenv
            
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
 Server address
    $ http://3.143.253.187/
