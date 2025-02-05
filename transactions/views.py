from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm

# Create your views here.


@login_required
def transactions(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm(user=request.user)
    
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions.html', {'form': form, 'transactions': transactions})

@login_required
def edit(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transaction, user=request.user)
    return render(request, 'edit_transaction.html', {'form': form})


@login_required
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    transaction.delete()
    return redirect('transactions')
