from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskFormModel

# Create your views here.
def home_page(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)

# create task
def add_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Task.objects.create(title=title, description=description, date=date)
        return redirect('home')
    
    return render(request, 'add.html')

# update task
def update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        # If the user submitted the form (POST), Django builds a form with
        form = TaskFormModel(request.POST, request.FILES, instance=task)
# request.POST (text data),
# request.FILES (for uploaded image),
# instance=book (we are updating this exact book).

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskFormModel(instance=task)
        context = {
            'task': task,
            'form': form
        }
        return render(request, 'update.html', context)


# details task
def details_home(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'details.html', {"task": task})
