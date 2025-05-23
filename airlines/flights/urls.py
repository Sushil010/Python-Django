from django.urls import path
from .import views

urlpatterns=[
    path('',views.flight,name="flight")
]