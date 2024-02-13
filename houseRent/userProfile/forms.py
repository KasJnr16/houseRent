from django import forms
from .models import ProfileInformation

class ProfileInformationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "py-4 px-6 rounded-xl border",
        "placeholder": "Enter first name"
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "py-4 px-6 rounded-xl border",
        "placeholder": "Enter last name"
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "py-4  rounded-xl border",  # Add your custom styling here
    }))

    class Meta:
        model = ProfileInformation
        fields = ("first_name", "last_name", "image")

