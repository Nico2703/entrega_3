from django import forms
from . import models

# class ProductoCategoriaForms(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()

class ClienteCategoriaForms(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-comtrol}"}),
            "apellido": forms.TextInput(attrs={"class":"form-comtrol}"}),
            "nacimiento": forms.TextInput(attrs={"class":"form-comtrol}"}),
        }