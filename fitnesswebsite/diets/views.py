from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Diet


@login_required
def client_diets(request):
    diets = Diet.objects.filter(trainer=request.user.trainer_profile)
    return render(request, 'diets/client_diets.html', {'diets': diets})
