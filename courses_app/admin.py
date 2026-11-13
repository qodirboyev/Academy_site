from django.contrib import admin
from .models import Courses,Lessons,Teachers
# Register your models here.

admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Teachers)
