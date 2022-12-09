# Introduction

The goal of this project is to provide minimalistic django project template that iha create project

Template is written with django 4.1.2 and python 3.8 in mind.
Docker version 20.10.20

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Deployment AWS ubuntu 

* Separated requirements files

* PostgresSQL by default if no env variable is set

{% endif %}


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
    
Docker up
    $ cd _development
    $ docker-compose up -d 
then checking all cotainer created
    $ docker ps -a
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    

