from django.shortcuts import render, redirect
from myapp.models import Users

# Create your views here.


def home(request):
    return render(request, 'mainpage.html')


def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['e-mail']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if re_password == password:
            if Users.objects.filter(email=email).exists():
                print('user with this email already exists!')
            else:
                user = Users.objects.create(name=name, surname=surname, email=email, password=password, role_id=2)
                user.save()
                print('user registered')
        else:
            print('passwords are not matching!')

        return redirect('/')

    else:
        return render(request, 'signup.html')


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


def login(request):
    return render(request, 'login.html')


def profile(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            print(user.name, user.email, user.surname)
            if password == user.password:
                return render(request, 'profile.html')
            else:
                print('password is not matching!')
                return redirect('/login?password_error')
        else:
            print('user with this email is not exist!')
    else:
        return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')
