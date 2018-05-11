from django import forms

from farmacia.models import Usuario
from .models import Producto, Factura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['folio', 'nombre','provedor','descripcion','cantidad','clasificacion','precio','descuento','factura',]
        labels={
            'folio': 'Folio',
            'nombre':'Nombre',
            'provedor':'Provedor',
            'descripcion': 'Descricpion Producto',
            'cantidad': 'Cantidad',
            'clasificacion': 'Clasificacion',
            'precio':'Precio',
            'descuento':'Descuento',
            'factura': 'Factura',
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model=Factura
        fields=['id','fechaEmision','monto','usuario']
        labels={
            'id':'ID',
            'fechaEmision': 'Fecha de Emision',
            'monto':'Monto',
            'usuario':'Cliente',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['password','username','correo','rfc','nombre','telefono']
        labels={
            'password':'Contraseña',
            'username':'Nombre de usuario',
            'correo':'correo',
            'rfc':'RFC',
            'nombre':'Nombre',
            'telefono':'Telefono',
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['password','username']
        labels={
            'username': 'Usuario',
            'password':'Contraseña',
        }
