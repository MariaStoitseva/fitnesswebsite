from django.urls import path
from .views import client_diets

urlpatterns = [
    path('client/diets/', client_diets, name='client_diets'),
]
