from django import forms
from .models import Diet, Meal


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['meals']
