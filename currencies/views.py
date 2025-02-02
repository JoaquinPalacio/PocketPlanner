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
    currencies = Currency.objects.all()
    context = {
        'currencies': currencies,
        'from_currency': request.POST.get('from_currency', 'USD'),
        'to_currency': request.POST.get('to_currency', 'EUR'),
        'amount': request.POST.get('amount', ''),
        'converted_amount': None
    }

    if request.method == 'POST':
        try:
            from_currency = request.POST['from_currency']
            to_currency = request.POST['to_currency']
            amount = float(request.POST['amount'])

            from_rate = Currency.objects.get(code=from_currency).rate_to_usd
            to_rate = Currency.objects.get(code=to_currency).rate_to_usd

            context['converted_amount'] = (amount/from_rate)*to_rate
        except (ValueError, Currency.DoesNotExist) as e:
            context['error'] = e
        
    return render(request, 'converter.html', context)


def update(request):
    return render(request, 'update.html')
