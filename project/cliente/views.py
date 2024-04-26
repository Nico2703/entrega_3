from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    if request.method == "POST":
        form = forms.ClienteCategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:
        form = forms.ClienteCategoriaForms()
    consulta_clientes = models.Cliente.objects.all()
    return render (request,"cliente/index.html", context={"form": form, "clientes": consulta_clientes})