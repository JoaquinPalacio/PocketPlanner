from django.shortcuts import render

# Create your views here.


def transactions(request):
    return render(request, 'transactions.html')


def detail(request):
    return render(request, 'detail.html')


def create(request):
    return render(request, 'create.html')


def edit(request):
    return render(request, 'edit.html')


def delete(request):
    return render(request, 'delete.html')
