from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "países"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}, {self.precio}"
    
    class Meta:
        verbose_name_plural = "productos"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "país de origen")
    producto_adquirido = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "producto")

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.pais_origen_id}, {self.nacimiento}"
