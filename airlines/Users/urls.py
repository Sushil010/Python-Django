from django.urls import path
from . import views

urlpatterns=[
    path('',views.main_page,name="index"),
    path('login/',views.login_method,name="login"),
    path('logout/',views.logout_method,name="logout")
]