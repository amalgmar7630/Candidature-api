# ApplicationTest

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.1.2 and Django 3.1.5. User admin should login with the credentientials that he 
has created with createsuperuser to see the admin interface, otherwise simple user can register and login to create application.

## API server

Create a Virtual Environnment with Python 3

Install PostgreSQL

Install the backend requirements by rununing pip install -r requirememts.txt

Set some customized environnement variables in setting.py file
       
       EMAIL_HOST_USER = 'email'
       EMAIL_HOST_PASSWORD = 'password'
       PASSWORD: 'postgres'
       USER: 'postgres'

Run python manage.py makemigrations to create new migrations based on the changes you have made to your models

Run python manage.py migrate to apply migrations

Create Super User to affect specific features for him by running python manage.py createsuperuser
