from django.shortcuts import render
from .models import Currency
from .services import update_currency_rates
from django.contrib.auth.decorators import permission_required
from django.db.models import Q


# Create your views here.


def all_currencies(request):
    query = request.GET.get('q', '')
    currencies = Currency.objects.all()
    
    if query:
        currencies = currencies.filter(Q(code__icontains=query) | Q(name__icontains=query))
    
    context = {
        'currencies': currencies,
        'last_updated': Currency.objects.first().updated_at if Currency.objects.exists() else None,
        'query': query,
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


@permission_required('currencies.can_update_rates', raise_exception=True)
def update(request):
    if request.method == 'POST':
        success, message = update_currency_rates()
        if success:
            return render(request, 'update_currencies.html', {'message': message})
        else:
            return render(request, 'update_currencies.html', {'error': message})
    return render(request, 'update_currencies.html')
