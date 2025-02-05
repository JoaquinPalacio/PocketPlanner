from django import forms
from .models import Transaction
from categories.models import Category
from currencies.models import Currency
from django.core.exceptions import ValidationError


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type_transaction', 'category', 'currency']
        widgets = {
            'type_transaction': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'category': forms.Select(attrs={
                'class': 'form-select select2-search',
                'required': False
            }),
            'currency': forms.Select(attrs={
                'class': 'form-select select2-search',
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)
            self.fields['currency'].queryset = Currency.objects.all()
            
            self.fields['amount'].widget.attrs.update({
            'class': 'form-control',
            'step': '0.01',
            'placeholder': '0.00'
            })

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None:
            raise ValidationError("Amount must be positive")
        if amount < 0:
            raise ValidationError("Amount must be positive")
        return amount