from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_pedido', 'producto', 'cantidad', 'estado']
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'type': 'date'}),
        }


