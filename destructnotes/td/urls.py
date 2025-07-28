from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.forms,name="forms"),
    path('delete/<int:ids>',views.delete_tasks,name='delete_tasks'), #this ids variable
    # should match what we are passing to delete_tasks in views
    path('update/<int:ids>',views.edit_tasks,name='update'),
    path('check/<int:ids>',views.comp_tasks,name='check')
    
    # path('lists/')
]