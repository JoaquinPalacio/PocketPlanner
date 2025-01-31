from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm

# Create your views here.


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registro exitoso.')
                return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Sesión cerrada.')
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'update.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Perfil eliminado.')
        return redirect('home')
    return render(request, 'delete.html')
