from .models import Create
from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Create_form(forms.ModelForm):

    class Meta:
        model = Create
        fields = ['title', 'content', 'tags']
        
