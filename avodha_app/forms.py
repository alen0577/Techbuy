from .models import Shop
from django import forms


class ModelForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'des', 'img', 'price']

