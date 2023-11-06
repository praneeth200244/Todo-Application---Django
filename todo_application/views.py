from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
from django.shortcuts import render
from .models import Task

def addTask(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task is not None:
            Task.objects.create(task=task)
    return redirect('home')
   
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        edited_task = request.POST.get('task')
        get_task.task = edited_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render (request, 'edit_task.html', context)

def delete_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')


