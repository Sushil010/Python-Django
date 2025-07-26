from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.forms,name="forms"),
    path('delete/<int:ids>',views.delete_tasks,name='delete_tasks')
    # path('lists/')
]