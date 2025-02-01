from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from currencies.models import Currency

class CustomSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    base_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        required=True,
        label="Base currency"
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'base_currency')

class UpdateProfileForm(forms.ModelForm):
    base_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        required=True,
        label="Moneda Base"
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'base_currency']