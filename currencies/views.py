from django.shortcuts import render

# Create your views here.


def all_currencies(request):
    return render(request, 'currencies.html')


def converter(request):
    return render(request, 'converter.html')


def update(request):
    return render(request, 'update.html')
