from django.urls import path
from .views import home, delete, add

urlpatterns = [
    path('', home),
    path('<uuid:uuid>/delete/', delete),
    path('add/', add)
]
