from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyUserForm(UserCreationForm):
    class Meta:
        ##It should be model not models
        model = MyUser
        fields = ['first_name','last_name','email','role']
        widgets={
        'first_name':forms.TextInput(attrs={'style':'color:red'})
        }