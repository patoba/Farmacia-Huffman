from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    correo = models.CharField(max_length=25)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=40)
    telefono=models.CharField(max_length=12)
    admin=models.BooleanField(default=False)

# Create your models here. Va
class Factura(models.Model):
    fechaEmision=models.DateField(default=timezone.now)
    usuario=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)

class Producto(models.Model):
    folio=models.CharField(max_length=12,primary_key=True)
    nombre=models.CharField(max_length= 12)
    provedor=models.CharField(max_length=12)
    descripcion=models.TextField()
    cantidad = models.IntegerField()
    clasificacion=models.CharField(max_length=12)
    precio = models.FloatField()
    descuento = models.IntegerField(default=0)
    factura = models.ForeignKey(Factura, null=True, blank=True, on_delete=models.CASCADE)
