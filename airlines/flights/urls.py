from django.urls import path
from .import views

urlpatterns=[
    path('',views.flight,name="flight"),
    path('<int:flight_id>',views.getDetails,name="get_details")
]