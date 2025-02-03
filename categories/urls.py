from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('<id>', views.detail, name='detail_category'),
    path('<id>/edit/', views.edit, name='edit_category'),
    path('<id>/delete/', views.delete, name='delete_category'),
]
