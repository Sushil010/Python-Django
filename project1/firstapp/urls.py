
from django.urls import path
from . import views



urlpatterns = [
    path('',views.first_app,name='first_app'),
    path('<int:aero_id>/',views.aero_desc,name='aero_desc'),
    path('pil_info/',views.pil_info,name='pil_info'),
]