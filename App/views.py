from django.db.models import Sum
from django.shortcuts import render
from transactions.models import Transaction
from currencies.models import Currency

def calculate_category_totals(transactions, base_currency):
    category_totals = {}
    for transaction in transactions:
        if transaction.currency:
            amount_in_base = (transaction.amount / transaction.currency.rate_to_usd) * base_currency.rate_to_usd
            category_name = transaction.category.name if transaction.category else "No category"
            if category_name not in category_totals:
                category_totals[category_name] = 0
            category_totals[category_name] += amount_in_base
    return category_totals

def home(request):
    if request.user.is_authenticated:
        withdrawals = Transaction.objects.filter(
            user=request.user, type_transaction='withdrawal'
        ).select_related('currency', 'category')
        deposits = Transaction.objects.filter(
            user=request.user, type_transaction='deposit'
        ).select_related('currency', 'category')

        base_currency = request.user.base_currency
        category_totals_withdrawals = calculate_category_totals(withdrawals, base_currency)
        category_totals_deposits = calculate_category_totals(deposits, base_currency)

        chart_data_withdrawals = {
            'labels': list(category_totals_withdrawals.keys()),
            'data': list(category_totals_withdrawals.values()),
        }
        chart_data_deposits = {
            'labels': list(category_totals_deposits.keys()),
            'data': list(category_totals_deposits.values()),
        }

        if not chart_data_deposits['data']:
            chart_data_deposits = {'labels': ['No Data'], 'data': [1]}
    else:
        chart_data_withdrawals = {'labels': [], 'data': []}
        chart_data_deposits = {'labels': [], 'data': []}

    return render(request, 'home.html', {
        'chart_data': chart_data_withdrawals,
        'chart_data_deposits': chart_data_deposits,
    })