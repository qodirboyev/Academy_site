from django.shortcuts import render
from .models import Courses
# Create your views here.




def courses_view(request):
    tempalte_name = 'courses_app/courses.html'
    context = {
        "courses" : Courses.objects.all()
    }
    return render(request, tempalte_name, context)
