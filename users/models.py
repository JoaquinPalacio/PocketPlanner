from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    base_currency = models.ForeignKey(
        'currencies.Currency', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
