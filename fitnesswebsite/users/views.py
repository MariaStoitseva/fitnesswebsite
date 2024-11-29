from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        # Automatically log in the user after registration
        user = form.save()
        login(self.request, user)
        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('dashboard')  # Redirect to the dashboard after login
