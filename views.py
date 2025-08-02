from django.shortcuts import render

def dashboard_view(request):
    tasks = [
        {'title': 'Setup Django Project', 'description': 'Initialize Django project structure', 'completed': True},
        {'title': 'Create Dashboard App', 'description': 'Develop dashboard app module', 'completed': True},
        {'title': 'Design Task Model', 'description': 'Define Task model fields', 'completed': True},
        {'title': 'Admin Panel', 'description': 'Manage tasks in admin panel', 'completed': True},
    ]
    return render(request, 'dashboard.html', {'tasks': tasks})


