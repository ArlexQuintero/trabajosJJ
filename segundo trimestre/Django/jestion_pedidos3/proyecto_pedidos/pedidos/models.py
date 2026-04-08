from django.db import models
from django.utils import timezone
import datetime

class Cliente(models.Model):
    nombre    = models.CharField(max_length=100)
    correo    = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    telefono  = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock  = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Pedido(models.Model):
    ESTADOS_CHOICES = [
        ('pendiente',  'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado',    'Enviado'),
        ('entregado',  'Entregado'),
        ('cancelado',  'Cancelado'),
    ]
    cliente      = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_pedido = models.DateField(null=True, blank=True)
    estado       = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')
    creado_en    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} — {self.cliente}"

    # Total calculado sumando los subtotales de los detalles
    def total(self):
        return sum(d.subtotal() for d in self.detalles.all())

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    def tiempo_desde_creacion(self):
        """Retorna las horas transcurridas desde que se creó el pedido."""
        if not self.creado_en:
            return 0
        diferencia = timezone.now() - self.creado_en
        return diferencia.total_seconds() / 3600

    def puede_editar_completo(self):
        """True si han pasado menos de 2 horas desde la creación."""
        return self.tiempo_desde_creacion() < 2

    def puede_editar_completo(self):
        """True si han pasado menos de 2 horas desde la creación."""
        return self.tiempo_desde_creacion() < 2

    def esta_bloqueado(self):
        """True si el pedido está cancelado — no se puede editar nada."""
        return self.estado == 'cancelado'


class DetallePedido(models.Model):
    pedido     = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto   = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad   = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedido'