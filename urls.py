from django.contrib import admin
from django.urls import path
from dashboard_module import views  # <-- Import your view here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),  # <-- Add this line
]
