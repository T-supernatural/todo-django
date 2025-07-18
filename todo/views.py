from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Create your views here.
def home_page(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)

def add_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('home')
    
    return render(request, 'add.html')