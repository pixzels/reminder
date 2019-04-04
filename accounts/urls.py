from django.contrib import admin
from django.urls import path
from .views import login, signup, logout

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),
]
