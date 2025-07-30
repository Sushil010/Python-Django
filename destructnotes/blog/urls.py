from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('create/',views.create_post,name="create_post"),
    path('delete/<int:idx>',views.delete_posts,name="delete_post"),
    path('edit/<int:idx>',views.edit_posts,name="edit")
]
