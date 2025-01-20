from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('<id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<id>/edit/', views.edit, name='edit'),
    path('<id>/delete/', views.delete, name='delete'),
]
