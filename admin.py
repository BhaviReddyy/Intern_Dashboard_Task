from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task  # <-- Import Task Model

# Register Task model to appear in admin
admin.site.register(Task)
