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


def profile(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if Users.objects.filter(email=email).exists():
            user = getUser(email)
            print(user.name, user.email, user.surname)
            if password == user.password:
                return render(request, 'profile.html', {'user': user})
            else:
                print('password is not matching!')
                return redirect('/login?password_error')
        else:
            print('user with this email is not exist!')
    else:
        return render(request, 'profile.html', {'user': request.user})


def contact(request):
    return render(request, 'contact.html')


def getUser(email):
    return Users.objects.get(email=email)
