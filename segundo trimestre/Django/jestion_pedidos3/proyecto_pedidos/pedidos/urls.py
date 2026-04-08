from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # ── Login / Logout ────────────────────────────────────────
    path('', views.login_view, name='login'),          # ← pantalla inicial
    path('logout/', views.logout_view, name='logout'),

    # ── CRUD Pedidos ──────────────────────────────────────────
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/', views.ver_pedido, name='ver_pedido'),
    path('pedidos/editar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('pedidos/exportar-pdf/', views.exportar_pedidos_pdf, name='exportar_pedidos_pdf'),
    
    # ── Clientes ──────────────────────────────────────────────
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    # ── Productos ─────────────────────────────────────────────
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # ── Exportar PDF ──────────────────────────────────────────────
    path('pedidos/exportar-pdf/',   views.exportar_pedidos_pdf,   name='exportar_pedidos_pdf'),
    path('clientes/exportar-pdf/',  views.exportar_clientes_pdf,  name='exportar_clientes_pdf'),
    path('productos/exportar-pdf/', views.exportar_productos_pdf, name='exportar_productos_pdf'),
    
    # ── Exportar Excel ────────────────────────────────────────────
    path('pedidos/exportar-excel/',   views.exportar_pedidos_excel,   name='exportar_pedidos_excel'),
    path('clientes/exportar-excel/',  views.exportar_clientes_excel,  name='exportar_clientes_excel'),
    path('productos/exportar-excel/', views.exportar_productos_excel, name='exportar_productos_excel'),

    # ── API JWT ───────────────────────────────────────────────
    path('api/auth/login/',   views.LoginView.as_view(),  name='api_login'),
    path('api/auth/logout/',  views.LogoutView.as_view(), name='api_logout'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/me/',      views.ProfileView.as_view(), name='profile'),
]