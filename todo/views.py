from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home_page(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)

# create task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Or wherever your list view is
    else:
        form = TaskForm()
    return render(request, 'add.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    today = []
    upcoming = []
    previous = []
    completed = []

    for task in tasks:
        if task.is_completed:
            completed.append(task)
        elif task.is_today():
            today.append(task)
        elif task.is_upcoming():
            upcoming.append(task)
        elif task.is_previous():
            previous.append(task)

    return render(request, 'home.html', {
        'today': today,
        'upcoming': upcoming,
        'previous': previous,
        'completed': completed,
    })
