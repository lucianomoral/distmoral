from datetime import time
from django.db import models
from django.utils import timezone

# Create your models here.

class ListaPrecio (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class ListaPrecioLinea (models.Model):
    id = models.AutoField(primary_key=True)
    idListaPrecio = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT)
    idProducto = models.ForeignKey("Producto", on_delete=models.PROTECT)
    costo = models.DecimalField(decimal_places=2, max_digits=20)
    moneda = models.CharField(max_length=3)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    fecha_hora = models.DateTimeField(default=timezone.now())

class Producto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idGrupo = models.ForeignKey("GrupoProducto", on_delete=models.PROTECT)
    idFamilia = models.ForeignKey("FamiliaProducto", on_delete=models.PROTECT)
    unidad = models.CharField(max_length=10)
    cantPorBulto = models.IntegerField()

class GrupoProducto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class FamiliaProducto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    moneda = models.CharField(max_length=3)
    idListaPrecioDefault = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class PedidoVenta (models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.PROTECT)
    idListaPrecio = models.ForeignKey("ListaPrecio", on_delete=models.PROTECT)
    fecha = models.DateField(default=timezone.now())

class PedidoVentaLinea (models.Model):
    id = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey("PedidoVenta", on_delete=models.PROTECT)
    idProducto = models.ForeignKey("Producto", on_delete=models.PROTECT)
    cantidad = models.DecimalField(decimal_places=2, max_digits=20)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    moneda = models.CharField(max_length=3)
