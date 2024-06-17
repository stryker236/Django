from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.



def create(request):
    if request.method == 'POST':
        print(request.POST)
        Task.objects.create(title=request.POST['title'],
                            description = request.POST['description']
                            )
        return redirect('tasks')
    return render(request, 'create.html')

def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.completed = 'completed' in request.POST
        print(request.POST)
        task.save()
        return redirect('tasks')
    return render(request, 'update.html', {'task': task})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'delete.html', {'task': task})    

def home(request):
    return render(request, 'home.html')

def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html',context)

def detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task
    }
    return render(request, 'detail.html', context)
