from django.shortcuts import render
from .models import Students
from django.views.generic import ListView
# Create your views here.


class StudentsListView(ListView):
    model = Students
    context_object_name = 'student'
    template_name = 'students_app/students.html'
