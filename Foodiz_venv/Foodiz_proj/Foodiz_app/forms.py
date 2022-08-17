
from .models import Recipe
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
# Recipe Form 
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['food_name', 'recipe', 'image', 'category','ingredient']

# Register Form  
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "password": forms.PasswordInput(),
        }

# Login Form  
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
     ##?##
    
    