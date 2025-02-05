from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Category

# Create your views here.

@login_required
def all_categories(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    if request.method == 'POST':
        name = request.POST['name']
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'categories.html', {'categories': categories})
        
        if not (Category.objects.filter(name__iexact=name, user=user).exists()):
            Category.objects.create(name=name, user=user)
            return render(request, 'categories.html', {'categories': categories})
        
        messages.error(request, 'Category already exists.')

    return render(request, 'categories.html', {'categories': categories})



@login_required
def edit(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        name = request.POST['name']
        category.name = name
        category.save()
        return redirect('detail_category', id=category.id)
    return render(request, 'edit_category.html', {'category': category})


@login_required
def delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')
