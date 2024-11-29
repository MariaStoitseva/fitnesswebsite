from django.urls import path
from .views import customer_dashboard, trainer_dashboard

urlpatterns = [
    path('dashboard/', customer_dashboard, name='dashboard'),
    path('trainer/dashboard/', trainer_dashboard, name='trainer_dashboard'),
]
