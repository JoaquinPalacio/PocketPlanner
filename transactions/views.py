from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TrasactionForm

# Create your views here.


@login_required
def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions.html', {'transactions': transactions})


@login_required
def detail(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    return render(request, 'detail.html', {'transaction': transaction})


@login_required
def create(request):
    if request.method == 'POST':
        form = TrasactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
    else:
        form = TrasactionForm(user=request.user)
    return render(request, 'create.html', {'form': form})


@login_required
def edit(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    if request.method == 'POST':
        form = TrasactionForm(
            request.POST, instance=transaction, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TrasactionForm(instance=transaction, user=request.user)
    return render(request, 'edit.html', {'form': form})


@login_required
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions')
    return render(request, 'delete.html', {'transaction': transaction})
