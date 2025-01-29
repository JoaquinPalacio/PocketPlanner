from django import forms
from .models import Transaction


class TrasactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type_transaction', 'category', 'currency']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = user.category_set.all()
            self.fields['currency'].queryset = user.currency_set.all()
