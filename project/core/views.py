from django.shortcuts import render
from . import models
from cliente import models


def home(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        query = models.Cliente.objects.filter(apellido__icontains=consulta)
    else:
        query =  models.Cliente.objects.all()
    
    context = {"clientes": query}
    return render(request, "core/index.html", context)