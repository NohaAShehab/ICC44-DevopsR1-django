from django.db import models

# Create your models here.


### ORM --> object relational mapper
""" 
TABLE  --> CLASS

RECORD on the table  -->  represnet OBJECT FROM THE CLASS 
from students.models import Student
>>> s = Student()
>>> s.name='hosam'
>>> s.email='hosam@gmail.com'
>>> s.grade = 100
>>> s.photo='pic1.png'
>>> s.save()

"""

class Student(models.Model):  # table
    """ create columns with suitable datatypes --/ properties """
    """ when you create column via django default not null"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    grade = models.IntegerField(default=100)
    photo = models.CharField(max_length=100, null=True)

