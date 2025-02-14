from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.task_field,name='task'),
    # path('index/',views.index,name='index'),
    # path('task/',views.task_field,name='task')
]