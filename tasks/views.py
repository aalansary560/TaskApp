from django.shortcuts import render, redirect
from .models import Tasks
from .forms import AddTask

# Create your views here.

def addTask(request):
    tasks = Tasks.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = AddTask()
    context = {'tasks':tasks, 'form':form}
    return render(request, 'addTask.html', context)
