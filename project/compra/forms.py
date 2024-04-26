from django import forms
from . import models

# class ProductoCategoriaForms(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()

class CompraCategoriaForms(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = "__all__"
        widgets = {
            "producto": forms.TextInput(attrs={"class":"form-comtrol}"}),
            "precio": forms.TextInput(attrs={"class":"form-comtrol}"}),
        }