from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/',)
    path('',views.show_notes,name='show_notes'),
    path('home/', views.note_form, name='home'),
    path('view/<str:note_id>/',views.view_note,name='view_note')
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]

