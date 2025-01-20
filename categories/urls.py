from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('create/', views.create, name='create'),
    path('<id>', views.detail, name='detail'),
    path('<id>/edit/', views.edit, name='edit'),
    path('<id>/delete/', views.delete, name='delete'),
]
