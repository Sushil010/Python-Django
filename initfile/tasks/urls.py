from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("todos/",views.tasks,name="todos"),
    path("add_tasks/",views.add_tasks,name="add_tasks")
]