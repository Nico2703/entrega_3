from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    consulta_compra = models.Compra.objects.all()
    context = {"compra": consulta_compra}
    return render(request, "compra/index.html", context)