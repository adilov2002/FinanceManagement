from django.shortcuts import render, redirect
from myapp.models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if True:
            user = Users.objects.get(email=email)
            print(user, user.password)
            # print(user.name, user.email, user.surname)
            my_user = authenticate(email=user.email, password=user.password)
            print(my_user)
            if my_user:
                return redirect('/finance/profile/')
            else:
                print('password is not matching!')
                return redirect('/login?password_error')
        else:
            print('user with this email is not exist!')
    return render(request, 'login.html')


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
    return render(request, 'signup.html')


def logout(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')
