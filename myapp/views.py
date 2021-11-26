from django.shortcuts import render, redirect
from myapp.models import Users


def home(request):
    return render(request, 'mainpage.html')


def about(request):
    users_data = {
        'zhanniyet': {'fullname': 'Adilov Zhanniyet',
                      'url': 'zhanniyet',
                      'email': 'joni.2002.08@gmail.com',
                      'phone': '+7 (777) 888 60 80',
                      'position': 'Team Leader'},
        'sabyr': {'fullname': 'Shatekov Sabyr',
                  'url': 'sabyr',
                  'email': 'sabyr@gmail.com',
                  'phone': '+7 (777) 500 60 90',
                  'position': 'Developer'},
    }
    return render(request, 'about.html', {"dict": users_data})


def contact(request):
    return render(request, 'contact.html')
