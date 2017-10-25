from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def home(request):
    form = TaskForm(request.POST or None)
    task = Task.objects.all().order_by('-id')
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'home/home.html', locals())

def aktive(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_active = True
    task.save()
    return redirect('/home')

def dell(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/home')