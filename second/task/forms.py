from django import forms
from .models import TodoItems
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoItems
        fields=['title','completed']


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')