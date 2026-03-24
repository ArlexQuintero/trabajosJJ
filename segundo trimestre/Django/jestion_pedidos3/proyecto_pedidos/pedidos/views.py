from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido
from .forms import PedidoForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Crear las vistas para las operaciones CRUD
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/crear_pedido.html', {'form': form})


def ver_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedidos/ver_pedido.html', {'pedido': pedido})


def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/actualizar_pedido.html', {'form': form, 'pedido': pedido})


def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)

    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedidos')

    return render(request, 'pedidos/eliminar_pedido.html', {'pedido': pedido})
    #crear el pdf

def exportar_pedidos_pdf(request):
    pedidos = Pedido.objects.all()

    template = get_template('pedidos/pedidos_pdf.html')
    html = template.render({'pedidos': pedidos})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pedidos.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)

    return response