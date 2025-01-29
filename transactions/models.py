from django.db import models
from django.conf import settings

# Create your models here.


class Transaction(models.Model):
    types = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer'),
    ]
    amount = models.FloatField()
    type_transaction = models.CharField(max_length=10, choices=types)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.ForeignKey(
        'currencies.Currency', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.type_transaction} - {self.amount} - {self.currency.code}"
