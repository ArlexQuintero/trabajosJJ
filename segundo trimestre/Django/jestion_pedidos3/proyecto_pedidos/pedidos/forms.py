from django import forms
from .models import Cliente, Producto, Pedido, DetallePedido
from datetime import date
import re


class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nombre', 'correo', 'direccion', 'telefono']
        widgets = {
            'nombre':    forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
                'minlength': '3',
                'maxlength': '100',
            }),
            'correo':    forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa',
                'minlength': '5',
                'maxlength': '200',
            }),
            'telefono':  forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3001234567',
                'minlength': '7',
                'maxlength': '15',
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras y espacios.')
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').strip()
        if not re.match(r'^\d{7,15}$', telefono):
            raise forms.ValidationError('El teléfono debe tener entre 7 y 15 dígitos numéricos.')
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo', '').strip().lower()
        if not correo:
            raise forms.ValidationError('El correo es obligatorio.')
        qs = Cliente.objects.filter(correo=correo)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Ya existe un cliente con este correo.')
        return correo

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion', '').strip()
        if len(direccion) < 5:
            raise forms.ValidationError('La dirección debe tener al menos 5 caracteres.')
        return direccion


class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ['nombre', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto',
                'minlength': '2',
                'maxlength': '100',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0.01',
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': '0',
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s\-\_\.]+$', nombre):
            raise forms.ValidationError('El nombre contiene caracteres no permitidos.')
        qs = Producto.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Ya existe un producto con ese nombre.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None:
            raise forms.ValidationError('El precio es obligatorio.')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        if precio > 99999999.99:
            raise forms.ValidationError('El precio es demasiado alto.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None:
            raise forms.ValidationError('El stock es obligatorio.')
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        if stock > 999999:
            raise forms.ValidationError('El stock ingresado es demasiado alto.')
        return stock


class PedidoForm(forms.ModelForm):
    class Meta:
        model  = Pedido
        fields = ['cliente', 'fecha_pedido', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-control',
            }),
            'fecha_pedido': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'estado': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Muestra solo clientes activos
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['cliente'].empty_label = '— Selecciona un cliente —'
        # Formato de fecha para que aparezca al editar
        self.fields['fecha_pedido'].input_formats = ['%Y-%m-%d']

    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente')
        if not cliente:
            raise forms.ValidationError('Debes seleccionar un cliente.')
        return cliente

    def clean_fecha_pedido(self):
        fecha = self.cleaned_data.get('fecha_pedido')
        if not fecha:
            raise forms.ValidationError('La fecha del pedido es obligatoria.')
        if fecha < date.today():
            raise forms.ValidationError('La fecha del pedido no puede ser en el pasado.')
        return fecha

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        estados_validos = ['pendiente', 'procesando', 'enviado', 'entregado', 'cancelado']
        if estado not in estados_validos:
            raise forms.ValidationError('Estado no válido.')
        return estado


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model  = DetallePedido
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 9999,
            }),
        }

    # ── __init__ FUERA de Meta — este era el bug principal ──
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset    = Producto.objects.filter(stock__gt=5)
        self.fields['producto'].empty_label = '— Selecciona un producto —'

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None:
            raise forms.ValidationError('La cantidad es obligatoria.')
        if cantidad < 1:
            raise forms.ValidationError('La cantidad debe ser al menos 1.')
        if cantidad > 9999:
            raise forms.ValidationError('La cantidad no puede superar 9999 unidades.')
        return cantidad

    def clean_producto(self):
        producto = self.cleaned_data.get('producto')
        if not producto:
            raise forms.ValidationError('Debes seleccionar un producto.')
        return producto