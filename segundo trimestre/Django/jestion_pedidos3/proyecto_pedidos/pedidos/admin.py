from django.contrib import admin
from .models import Cliente, Producto, Pedido, DetallePedido

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(DetallePedido)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha_pedido', 'estado', 'total']