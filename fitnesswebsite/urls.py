from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitnesswebsite.public.urls')),
    path('users/', include('fitnesswebsite.users.urls')),
    path('workouts/', include('fitnesswebsite.workouts.urls')),
    path('diets/', include('fitnesswebsite.diets.urls')),
]
