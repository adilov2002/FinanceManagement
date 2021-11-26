from django.shortcuts import render, redirect
from myapp.models import Users


def login(request):
    if request.method == 'POST':
        pass
    else:
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

    else:
        return render(request, 'signup.html')


def logout(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'login.html')
