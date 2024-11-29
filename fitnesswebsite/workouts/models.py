from django.db import models
from fitnesswebsite.users.models import TrainerProfile, User


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercises/')
    equipment = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()


class Workout(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise)


class Class(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()
    clients = models.ManyToManyField(User, related_name='classes')


class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100)
    workouts = models.ManyToManyField(Workout)
