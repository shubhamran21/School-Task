from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('studentsignup/',views.studentsignup, name='studentsignup'),
    path('teachersignup/',views.teachersignup, name='teachersignup'),
    path('studentdashboard/',views.studentdashboard, name='studentdashboard'),
    path('teacherdashboard/',views.teacherdashboard, name='teacherdashboard'),
    path('studentlogin/',views.studentlogin, name='studentlogin'),
    path('teacherlogin/',views.teacherlogin, name='teacherlogin'),
    path('admindashboard/',views.admindashboard, name='admindashboard'),
    path('photo/',views.photo, name='photo'),
    path('studentphoto/',views.studentphoto, name='studentphoto'),
    path('teacherphoto/',views.teacherphoto, name='teacherphoto'),
    
]
