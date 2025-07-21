# forms.py
from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_completed', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
