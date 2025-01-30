from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
