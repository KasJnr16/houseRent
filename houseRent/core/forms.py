from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TimeInput(
        attrs={
            "placeholder":"Your username",
            "class":"px-3 py-3 rounded-xl border border-black-100"
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Your email address",
            "class":"px-3 py-3 rounded-xl border border-black-100"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Enter Password",
            "class":"px-3 py-3 rounded-xl border border-black-100" 
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Confirm Password",
            "class":"px-3 py-3 rounded-xl border border-black-100"
        }
    ))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
    }))