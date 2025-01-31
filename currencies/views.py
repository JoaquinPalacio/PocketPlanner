from django.shortcuts import render
from .models import Currency

# Create your views here.


def all_currencies(request):
    currencies = Currency.objects.all()
    context = {
        'currencies': currencies,
        'last_updated': Currency.objects.first().updated_at if Currency.objects.exists() else None
    }
    return render(request, 'currencies.html', context)


def converter(request):
    return render(request, 'converter.html')


def update(request):
    return render(request, 'update.html')
