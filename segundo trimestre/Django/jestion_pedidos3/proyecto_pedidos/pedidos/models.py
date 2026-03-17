from django.db import models
class Pedido(models.Model):
    ESTADOS_CHOICES=[
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ]
    cliente = models.CharField(max_length=100)
    fecha_pedido = models.DateField(null=True,blank=True)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20,choices=ESTADOS_CHOICES, default='pendiente')

    def __str__(self):
        return f"Pedido de {self.cliente} -- {self.producto} ({self.id})" 