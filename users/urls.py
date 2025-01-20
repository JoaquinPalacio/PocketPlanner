from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signin/', views.signin_user, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
