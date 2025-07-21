from django import forms
from .models import Task

class TaskFormModel(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "date", "completed"]