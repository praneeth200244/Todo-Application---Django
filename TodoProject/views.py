from django.shortcuts import render
from todo_application.models import Task


def home(request):
    # tasks = Task.objects.filter(is_completed = False).order_by('updated_at')
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at') # Descending Order
    completed_tasks = Task.objects.filter(is_completed = True) # Descending Order
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request, 'home.html', context)