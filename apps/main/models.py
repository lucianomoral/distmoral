from datetime import time
from django.db import models
from django.utils import timezone

# Create your models here.

class ListaPrecio (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ListaPrecioLinea (models.Model):
    id = models.AutoField(primary_key=True)
    listaPrecio = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT)
    producto = models.ForeignKey("Producto", on_delete=models.PROTECT)
    costo = models.DecimalField(decimal_places=2, max_digits=20)
    moneda = models.CharField(max_length=3)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    fecha_hora = models.DateTimeField(default=timezone.now())

class Producto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    grupo = models.ForeignKey("GrupoProducto", on_delete=models.PROTECT, blank=True, null=True)
    familia = models.ForeignKey("FamiliaProducto", on_delete=models.PROTECT, blank=True, null=True)
    unidad = models.CharField(max_length=10)
    cantPorBulto = models.IntegerField()

    #def __str__(self):
    #    return self.nombre

class GrupoProducto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class FamiliaProducto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    moneda = models.CharField(max_length=3)
    listaPrecioDefault = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT, blank=True, null=True)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    #def __str__(self):
    #    return self.nombre

class PedidoVenta (models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.PROTECT)
    listaPrecio = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT)
    fecha = models.DateField(default=timezone.now())

class PedidoVentaLinea (models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey("PedidoVenta", on_delete=models.PROTECT)
    producto = models.ForeignKey("Producto", on_delete=models.PROTECT)
    cantidad = models.DecimalField(decimal_places=2, max_digits=20)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    moneda = models.CharField(max_length=3)
