from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def service(request):
    return render(request, 'pages/service.html')

def review(request):
    return render(request, 'pages/review.html')

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

