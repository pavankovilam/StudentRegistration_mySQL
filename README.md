# Install Django
``` pip install django pymysql ```
# Start Django project
``` django-admin startproject StdRegistration ```
# Navigate Into Project
``` cd StdRegistration ```
# Create New App
``` py manage.py startapp Registration ```
#### Add app in settings.py
# Create Templates Folder
#### cretate Templates folder in project level
Add This templates folder to settingss folder below BASE_DIR 
``` TEMPLATE_DIR = BASE_DIR/'templates' ```<br>
Now add this ``` TEMPLATE_DIR ``` to ``` TEMPLATES ``` at ``` DIRS```. <br>
Now open templates folder and create Sub folder with name of App that you created. <br>
In that sub folder create a file name ``` index.html``` and paste the form code without java script 
# Create DataBase 
Open MySQL commandline and create a new database <br>
``` CREATE DATABASE Django_practice; ``` 
# Configure DataBase in Django
Open Settings.py goto ``` DATABASES ``` and replace it with following code. <br>
And setup the correct user and Password <br>
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'Django_practice',
        'USER':'root',
        'PASSWORD':'xxxxxx',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
} 
```
Now open ``` __init.py__ ``` in ``` StdRegistration ``` and write following code.
``` 
import pymysql
pymysql.install_as_MySQLdb()
```
# Create Model
--> Open models.py and paste the following code. <br>
```
from django.db import models

class Student_data(models.Model):
    Name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=30)
    Phone = models.IntegerField() 
```
# Configuring Views.py
```
from django.shortcuts import render
from .models import Student_data
def index(request):
    if request.method =="POST":
        Std_Name = request.POST['name']
        Std_Email = request.POST['email']
        Std_Number = request.POST['phone']

        New_Student=Student_data(Name=Std_Name,email=Std_Email,Phone=Std_Number)
        New_Student.save()
    return render(request,"Registration/index.html")
```
# connfiguring URLS
Configure the url pattren
``` 
from django.contrib import admin
from django.urls import path
from Registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
]
```
# Now open command prompt
Run the following commands <br>
 ``` py manage.py make migrations ``` <br>
 ``` py manage.py migrate ``` <br>
 ``` py manage.py runserver ``` <br>
 Open the Url in any of the browser



