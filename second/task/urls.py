from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.task,name="task"),
    path('todos/',views.todos,name="todos"),
    path('<int:tweet_id>/deletetodo/',views.deletetodo,name='deletetodo')
]