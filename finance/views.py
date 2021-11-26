from django.shortcuts import render


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass
        return render(request, 'profile.html', {'user': request.user})
    else:
        return render(request, '404.html')
