from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Task

def dashboard_view(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard_module/dashboard.html', {'tasks': tasks})
