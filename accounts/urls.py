from django.contrib import admin
from django.urls import path
from .views import signup
from django.contrib.auth import views as django_auth_views


urlpatterns = [
    path('login/', django_auth_views.LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', django_auth_views.LogoutView.as_view()),
    path('signup/', signup),
]
