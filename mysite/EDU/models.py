from datetime import date
import email
from pydoc import classname
from typing import Optional
from unicodedata import name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.query_utils import Q



    


class Courses(models.Model):
    name=models.CharField(max_length=100)
    # codenumber=models.CharField(max_length=25)

    def get_lessons(self):
        return self.name




class Student(models.Model):
    name=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # photo=models.ImageField()

    def get_courses(self):
        class_list = self.enroll_set.all()
        return class_list
  
        
        


class Everything(models.Model):
    name=models.CharField(max_length=100,null=True)
    classcode=models.CharField(max_length=100,null=True)
    lecturer=models.CharField(max_length=100,null=True) 
    image = models.ImageField(null=True, blank=True)

    # birthdate=models.DateTimeField()
    # enrollmentdate=models.DateTimeField()




class Teacher(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=100)
    # created_at=
    coursecode=models.CharField(max_length=100)

class Enroll(models.Model):
    everything=models.ForeignKey(Everything,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    
    

    


class Lesson(models.Model):
     name= models.ForeignKey(Everything, null=True, on_delete=models.CASCADE)
     number=models.IntegerField(null=True)
     title=models.CharField(max_length=100,null=True)

class Profile(models.Model):
    image = models.ImageField(null=True, blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone= models.CharField(null=True,max_length=200)
    email= models.CharField(null=True,max_length=200)
    

        
        
        




    


