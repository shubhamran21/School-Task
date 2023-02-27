from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(Image)
admin.site.register(StudentImage)
admin.site.register(TeacherImage)
