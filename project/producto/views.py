from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaForms()
    consulta_productos = models.Producto.objects.all()
    return render(request,"producto/index.html", context={"form": form, "productos": consulta_productos})

