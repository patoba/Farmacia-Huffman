from django.urls import path, re_path
from . import views
from django.core.mail import EmailMessage
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    path('', views.index, name='inicio'),
    path('index/', views.index, name='inicio'),
    path('admin/producto/agregar',views.productos_agregar, name='productos_agregar'),
    path('registro',views.registro ,name="registro"),
    path('sesion',views.sesion ,name="sesion"),
    path('administrador',views.administrador ,name="administrador"),
    path('admin/productos',views.productos_all,name="productos_all"),
    path('admin/productos/cambiar<folio>',views.producto_cambiar,name="producto_cambiar"),
    path('admin/productos/eliminar<folio>',views.producto_eliminar,name="producto_eliminar"),
    path('admin/ventas/totales',views.ventas_totales,name="ventas_totales"),
    path('admin/ventas/parciales',views.ventas_parciales,name="ventas_parciales"),
    path('admin/inicio',views.admin_inicio,name="adminInicio"),
    path('admin/carrito',views.admin_carrito,name="adminCarrito"),
    path('facturas',views.factura,name="historia_facturas"),
    path('crearUsuario',views.registro,name="crear_usuario"),
    path('cerrarSesion',views.cerrarSesion,name="cerrarSesion"),
    path('contacto',views.contacto,name="contacto"),
    path('promocion',views.promocion,name="promocion"),
    path('miCuenta',views.miCuenta,name="micuenta"),
    path('productos',views.productos,name="productos"),
    path('generarFactura',views.agregarFactura,name="agregarFactura"),
    path('quitar_carrito<Id>',views.quitar_carrito,name="quitar_carrito"),
    path('anadir_carrito<Folio>',views.anadir_carrito,name="anadir_carrito"),
    path('login/recuperar',views.enviarCorreo,name="recuperarContrasena"),
]
