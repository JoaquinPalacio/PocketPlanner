from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import CustomUser
from currencies.models import Currency

# Create your views here.


def signup_user(request):
    currencies = Currency.objects.all()
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'currencies': currencies,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                selected_currency = request.POST['currency']
                currency_obj = Currency.objects.get(code=selected_currency)
                user = CustomUser.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'],
                    first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                    base_currency=currency_obj)
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                messages.error(request, 'El usuario ya existe.')
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'currencies': currencies,
                })
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'currencies': currencies,
            })


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            messages.error(request, 'Credenciales inválidas.')
            return render(request, 'login.html', {
                'form': AuthenticationForm(request.POST),
            })
        else:
            login(request, user)
            return redirect('profile')


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
