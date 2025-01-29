from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'base_currency']
