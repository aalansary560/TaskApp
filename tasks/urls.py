from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('addTask/', views.addTask, name='addTask')
]
