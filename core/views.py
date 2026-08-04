from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tasks.models import Tasks

@login_required(login_url='new')
def home(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks':tasks})

def new(request):
    return render(request, 'new.html')