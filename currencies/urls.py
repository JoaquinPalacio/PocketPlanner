from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_currencies, name='currencies'),
    path('converter/', views.converter, name='converter'),
    path('update/', views.update, name='update'),
]
