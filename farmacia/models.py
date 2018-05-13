from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    correo = models.EmailField(max_length=25)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=40)
    telefono=models.CharField(max_length=12)
    admin=models.BooleanField(default=False)
    def __str__(self):
        return "%d - %s" % (self.id, self.username)

# Create your models here. Va
class Factura(models.Model):
    fechaEmision=models.DateField(default=timezone.now)
    usuario=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    monto=models.FloatField(default=0)
    def __str__(self):
        return "%d - %s asosicada a %s" % (self.id,self.fechaEmision,self.usuario)

class Producto(models.Model):
    folio=models.CharField(max_length=4,primary_key=True)
    url=models.CharField(max_length=100)
    nombre=models.CharField(max_length= 100)
    provedor=models.CharField(max_length=40)
    descripcion=models.TextField()
    cantidad = models.IntegerField()
    clasificacion=models.CharField(max_length=40)
    precio = models.FloatField()
    descuento = models.IntegerField(default=0)
    total=models.FloatField(default=0)
    def __str__(self):
        return "%s - %s" % (self.folio,self.nombre)

class ProductoIndividual(models.Model):
    nombre=models.CharField(max_length= 100)
    provedor=models.CharField(max_length=40)
    clasificacion=models.CharField(max_length=40)
    precio = models.FloatField()
    descuento = models.IntegerField(default=0)
    factura = models.ForeignKey(Factura, null=True, blank=True, on_delete=models.CASCADE)
    total=models.FloatField(default=0)
    def __str__(self):
        return "%s - %s -> %s" % (self.id,self.nombre,self.factura)
