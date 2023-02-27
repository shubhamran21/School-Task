from django.db import models

class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=500)
    is_active=models.BooleanField(default=True)
    # image=models.ImageField(upload_to='photo')
    def __str__(self) -> str:
        return self.username

class student(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='media')
    def __str__(self) -> str:
        return self.sname
    
class teacher(models.Model):
    tname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=500) 
    image=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.tname


class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)


class StudentImage(models.Model):
 photo = models.ImageField(upload_to="myphoto")
 date = models.DateTimeField(auto_now_add=True)
 

class TeacherImage(models.Model):
 photo = models.ImageField(upload_to="mypic")
 date = models.DateTimeField(auto_now_add=True)
