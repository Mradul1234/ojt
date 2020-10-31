from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.utils import timezone
from .models import *
from .forms import TaskForm, TaskCommentForm, ProjectForm
     
# Create your views here.

def home(request):
    return render(request, 'task_manage/base.html', {'title':'home'})    

def project(request):
    project = Project.objects.all()

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')

    context = {'project' : project, 'title':'project','form':form }
    return render(request, 'task_manage/project.html', context)


def task(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(task_project=Project.objects.get(id=pk))
    task = Task.objects.filter(task_project=Project.objects.get(id=pk)).count()
    if not task:
        task = 1
    else:
        task = task + 1

    form = TaskForm(initial={'task_project':project, 'task_number':task})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task', kwargs={'pk':pk}))
            
    context = {'form':form,'tasks':tasks, 'task': task, 'project' : project, 'title':'task' }
    return render(request, 'task_manage/task.html', context)
    
    
def task_comment(request,pk):
    task = Task.objects.get(id=pk)
    task_comment = task.comments.all()

    form = TaskCommentForm(initial={'task':task})
    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_comment', kwargs={'pk':pk}))

    context={'form':form, 'title':'task_comment', 'task':task, 'task_comment':task_comment}
    return render(request, 'task_manage/task_comment.html', context)
    
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task', kwargs={'pk':pk}))

    context = {'form':form, 'title':'task' }
    return render(request, 'task_manage/task.html', context) 