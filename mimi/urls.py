from django.urls import path
from mimi.views import task_list

urlpatterns = [
    path('', task_list, name='task-list'),
]
