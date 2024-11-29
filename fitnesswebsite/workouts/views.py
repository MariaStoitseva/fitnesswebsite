from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def customer_dashboard(request):
    # Fetch workout and diet for the day
    return render(request, 'workouts/dashboard.html')


@login_required
def trainer_dashboard(request):
    # Fetch trainer-specific details
    return render(request, 'workouts/trainer_dashboard.html')
