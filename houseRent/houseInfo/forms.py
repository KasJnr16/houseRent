from django import forms
from .models import House

INPUT_CLASSES = "py-4 px-6 rounded-xl border "
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ("category", "house_name" ,"image", "image1", "image2", "price", "location", "description")

        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES, "placeholder": "House Category"}),
            "house_name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "House name"} ),
            "location": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Location"} ),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "placeholder": "House description"}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES, "placeholder": "Price"}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES, "placeholder": "Upload picture"}),
            "image1": forms.FileInput(attrs={"class": INPUT_CLASSES, "placeholder": "Upload picture"}),
            "image2": forms.FileInput(attrs={"class": INPUT_CLASSES, "placeholder": "Upload picture"}),
        }


