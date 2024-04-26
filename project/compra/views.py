from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    if request.method == "POST":
        form = forms.CompraCategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("compra:home")
    else:
        form = forms.CompraCategoriaForms()
    consulta_compras = models.Compra.objects.all()
    return render (request,"compra/index.html", context={"form": form, "compras": consulta_compras})