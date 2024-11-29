from django.db import models

from fitnesswebsite.users.models import TrainerProfile


class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()


class Diet(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
