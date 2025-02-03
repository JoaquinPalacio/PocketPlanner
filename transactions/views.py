from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TrasactionForm
from categories.models import Category
from currencies.models import Currency
from django.contrib import messages

# Create your views here.


@login_required
def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    currencies = Currency.objects.all()
    if request.method == 'POST':
        amount = request.POST['amount']
        type_transaction = request.POST['type_transaction']
        category_id = request.POST['category']
        currency_id = request.POST['currency']
        
        try:
            category = Category.objects.get(id=category_id)
            currency = Currency.objects.get(id=currency_id)
            Transaction.objects.create(amount=amount, type_transaction=type_transaction, category=category, currency=currency, user=request.user)
            return redirect('transactions')
        except Exception as e:
            messages.error(request, f"Error al crear la transacción: {e}")
    return render(request, 'transactions.html', {'transactions': transactions, 'categories': categories, 'currencies': currencies})


@login_required
def edit(request, id):
    categories = Category.objects.filter(user=request.user)
    currencies = Currency.objects.all()
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        amount = request.POST['amount']
        type_transaction = request.POST['type_transaction']
        category_id = request.POST['category']
        currency_id = request.POST['currency']
        try:
            category = Category.objects.get(id=category_id)
            currency = Currency.objects.get(id=currency_id)
            transaction.amount = amount
            transaction.type_transaction = type_transaction
            transaction.category = category
            transaction.currency = currency
            transaction.save()
            return redirect('transactions')
        except Exception as e:
            messages.error(request, f"Error al crear la transacción: {e}")

    return render(request, 'edit_transaction.html', {'transaction': transaction, 'categories': categories, 'currencies': currencies})


@login_required
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    transaction.delete()
    return redirect('transactions')
