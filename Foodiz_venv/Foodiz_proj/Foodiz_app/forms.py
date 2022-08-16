from dataclasses import field
import profile
from pyexpat import model
from tkinter import Widget
from .models import Recipe
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
# Recioe Form -- then creat a view
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['food_name', 'recipe', 'image', 'category','ingredient']

        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "password": forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,)
    widgets={"password": forms.PasswordInput()}