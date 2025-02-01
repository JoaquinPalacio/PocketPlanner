from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import CustomUser
from .forms import CustomSignupForm
from currencies.models import Currency

# Create your views here.


def signup_user(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomSignupForm()

    return render(request, 'signup.html', {
        'form': form,
        'currencies': Currency.objects.all()
    })


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Sesión cerrada.')
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def update_profile(request):
    currencies = Currency.objects.all()
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.username = request.POST["username"]
        selected_currency_code = request.POST.get("currency")
        if selected_currency_code:
            currency_obj = Currency.objects.get(code=selected_currency_code)
            user.base_currency = currency_obj

        user.save()

        return redirect("profile")

    return render(request, "update.html", {
        "user": user,
        "currencies": currencies
    })


@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Perfil eliminado.')
        return redirect('home')
    return render(request, 'delete.html')
