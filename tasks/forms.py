from django import forms
from .models import Tasks

class AddTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name']
