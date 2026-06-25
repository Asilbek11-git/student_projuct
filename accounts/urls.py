from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view,profile_view,home
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'),name="logout"),
    path('profile/', profile_view, name='profile'),
    path('',home,name='home'),
    
]