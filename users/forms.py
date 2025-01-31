from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name:
    #         raise forms.ValidationError('El nombre es obligatorio.')
    #     return name

    # def clean_lastname(self):
    #     lastname = self.cleaned_data.get('lastname')
    #     if not lastname:
    #         raise forms.ValidationError('El apellido es obligatorio.')
    #     return lastname


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'base_currency']
