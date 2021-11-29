from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def categories(request):
    group = None

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if group in 'user':
        return redirect('profile')
    if group in 'admin':
        return render(request, '')
