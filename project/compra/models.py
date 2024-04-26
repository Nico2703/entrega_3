from django.db import models
from producto.models import Producto
from cliente.models import Cliente


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "cliente")
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "producto")
    precio = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.cliente}, {self.producto}, {self.precio}"
    
    class Meta:
        verbose_name = "compra"
        verbose_name_plural = "compras"
