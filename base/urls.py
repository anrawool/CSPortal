from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/i', views.logoutUser, name="logout")
]