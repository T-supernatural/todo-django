from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Create your views here.
def home_page(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)