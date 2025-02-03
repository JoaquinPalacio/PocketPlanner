from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('<id>/edit/', views.edit, name='edit_transaction'),
    path('<id>/delete/', views.delete, name='delete_transaction'),
]
