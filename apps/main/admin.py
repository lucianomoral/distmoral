from django.contrib import admin
from .models import Cliente, ListaPrecio, ListaPrecioLinea, Producto, GrupoProducto, FamiliaProducto, PedidoVenta, PedidoVentaLinea

# Register your models here.

admin.site.register(Cliente)
admin.site.register(ListaPrecio)
admin.site.register(ListaPrecioLinea)
admin.site.register(Producto)
admin.site.register(GrupoProducto)
admin.site.register(FamiliaProducto)
admin.site.register(PedidoVenta)
admin.site.register(PedidoVentaLinea)