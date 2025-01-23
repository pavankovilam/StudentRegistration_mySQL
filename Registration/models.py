from django.db import models

# Create your models here.
class Student_data(models.Model):
    Name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=30)
    Phone = models.IntegerField()
