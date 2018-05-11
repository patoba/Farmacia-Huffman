from django.contrib import admin
from .models import Usuario,Factura,Producto

# Register your models here.
admin.site.register(Factura)
admin.site.register(Usuario)
admin.site.register(Producto)
