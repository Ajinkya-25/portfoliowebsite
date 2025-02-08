from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, 'portfolio/base.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    return render(request,'portfolio/projects.html')

def home(request):
    return render(request, 'portfolio/home.html')