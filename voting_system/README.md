# Django-Tutorial
First Django application tutorial


#To Create the Project

django-admin startproject <project-site-name>

#To create an app in the project.

python manage.py startapp polls {Must be in the same directory as the manage.py}


#To include a created app in the project, include the app.py class in settings.py INSTALLED APPS

e.g 'polls.apps.PollsConfig'	

#To create database, create models in the models.py of the app

then do migrations. e.g python manage.py migrate


#Templates

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument


