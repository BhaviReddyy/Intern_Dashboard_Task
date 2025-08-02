from django.contrib import admin
from django.urls import path
from dashboard_module import views  # Import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),  # Root URL to dashboard_view
]

