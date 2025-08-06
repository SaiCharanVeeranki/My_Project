from django import forms
from .models import Restarunts, Menu

class ResForm(forms.ModelForm):
    class Meta:
        model = Restarunts
        fields = ['res_name','Food_cat','rating','img','address']

# forms.py
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ['res']
