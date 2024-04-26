from django.shortcuts import render, redirect
from . import models, forms


def home(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Producto.objects.filter(nombre__icontains=consulta)
    else:
        query =  models.Producto.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)

def producto_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaForms()
    return render (request,"producto/producto_create.html", context={"form": form})