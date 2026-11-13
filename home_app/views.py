from django.shortcuts import render

# Create your views here.



def home(request):
    tempalte_name = 'home_app/home.html'
    return render(request, tempalte_name)