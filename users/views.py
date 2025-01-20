from django.shortcuts import render

# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    return render(request, 'logout.html')


def signin_user(request):
    return render(request, 'signin.html')


def profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    return render(request, 'update.html')


def delete_profile(request):
    return render(request, 'delete.html')
