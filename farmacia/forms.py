from django import forms

from farmacia.models import Usuario
from .models import Producto, Factura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['folio', 'nombre','provedor','descripcion','cantidad','clasificacion','precio','descuento']
        labels={
            'folio': 'Folio',
            'nombre':'Nombre',
            'provedor':'Provedor',
            'descripcion': 'Descricpion Producto',
            'cantidad': 'Cantidad',
            'clasificacion': 'Clasificacion',
            'precio':'Precio',
            'descuento':'Descuento',
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model=Factura
        fields=['id','fechaEmision','usuario']
        labels={
            'id':'ID',
            'fechaEmision': 'Fecha de Emision',
            'usuario':'Cliente',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['username','password','correo','rfc','nombre','telefono']
        labels={
            'username':'Nombre de Usuario',
            'password':'Contraseña',
            'correo':'Correo Electronico',
            'rfc':'RFC',
            'nombre':'Nombre',
            'telefono':'Telefono',
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['username','password']
        labels={
            'username': 'Usuario',
            'password':'Contraseña',
        }
