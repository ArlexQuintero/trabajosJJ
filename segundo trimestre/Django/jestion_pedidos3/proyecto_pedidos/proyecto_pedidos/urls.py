from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    # Redirección automática desde la raíz ("") hacia la vista listar_pedidos
    path('', lambda request: redirect('listar_pedidos')),  # 👈 Redirección automática
    # ruta que enlaza la URL /admin/ con el administrador intern
    path("admin/", admin.site.urls),
    # Inclusión de las rutas del módulo "pedidos"
    path("pedidos/", include("pedidos.urls")),
]
