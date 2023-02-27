from django import forms
from .models import Image,StudentImage,TeacherImage

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}
  
class StudentForm(forms.ModelForm):
 class Meta:
  model = StudentImage
  fields = '__all__'
  labels = {'photo':''}
  

class TeacherForm(forms.ModelForm):
 class Meta:
  model = TeacherImage
  fields = '__all__'
  labels = {'photo':''}