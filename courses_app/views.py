from django.shortcuts import render

# Create your views here.




def courses_view(request):
    tempalte_name = 'courses_app/courses.html'
    return render(request, tempalte_name)