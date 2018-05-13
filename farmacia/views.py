from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
import copy

from farmacia.forms import ProductoForm, UsuarioForm, LoginForm
from farmacia.models import Producto, Factura, Usuario, ProductoIndividual
from django.contrib import messages
from django.core.mail import EmailMessage

logeo=0

def importeParcial(producto):
    return producto.precio*producto.descuento*producto.cantidad/100

def index(request):
    return render(request,'farmacia/index.html')

def miCuenta(request):
    global logeo
    if logeo == 0:
        return render(request,'farmacia/miCuenta.html')
    usuario=Usuario.objects.get(username=logeo)
    if usuario.admin:
        producto=Producto.objects.order_by('folio')
        contexto={'productos':producto}
        return render(request, 'admin/productos_list.html', contexto)
        mensaje=Producto.objects.all()
        contexto={'mensaje':mensaje}
        return render(request, 'admin/miCuenta.html', contexto)
    facturaza=Factura.objects.filter(usuario=Usuario.objects.get(username=logeo)).order_by('-id')[:1].get()
    productos=ProductoIndividual.objects.filter(factura=facturaza)
    for indice in range(productos.count()):
        productos[indice].total=productos[indice].precio*(100-productos[indice].descuento)/100
        productos[indice].save()
    contexto={'usuarios':usuario,'productos':productos}
    return render(request,'cliente/miCuenta.html',contexto)

def admin_carrito(request):
    if logeo!=0:
        usuario=Usuario.objects.get(username=logeo)
        if usuario.admin:
            facturaza=Factura.objects.filter(usuario=Usuario.objects.get(username=logeo)).order_by('-id')[:1].get()
            productos=ProductoIndividual.objects.filter(factura=facturaza)
            for indice in range(productos.count()):
                productos[indice].total=productos[indice].precio*(100-productos[indice].descuento)/100
                productos[indice].save()
            contexto={'usuarios':usuario,'productos':productos}
            return render(request,'admin/carrito.html',contexto)
        return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no eres administrador'})
    return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no haz iniciado sesion'})


def admin_inicio(request):
    if logeo!=0:
        usuario=Usuario.objects.get(username=logeo)
        if usuario.admin:
            mensaje=Producto.objects.all()
            contexto={'mensaje':mensaje}
            return render(request, 'admin/miCuenta.html', contexto)
        return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no eres administrador'})
    return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no haz iniciado sesion'})

def quitar_carrito(request,Id):
    producto=ProductoIndividual.objects.get(id=Id)
    if request.method=='POST':
        producto.delete()
        return redirect('micuenta')
    return render(request, 'cliente/producto_eliminar.html', {'producto':producto})

def productos(request):
    if request.method =='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos_all')
    else:
        form=ProductoForm()
    return render(request, 'admin/producto_form.html', {'form':form})

def productos_all(request):
    if logeo!=0:
        usuario=Usuario.objects.get(username=logeo)
        if usuario.admin:
            producto=Producto.objects.order_by('folio')
            contexto={'productos':producto}
            return render(request, 'admin/productos_list.html', contexto)
        return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no haz iniciado sesion'})
    return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no haz iniciado sesion'})

def productos(request):
    return render(request,'farmacia/producto_card.html',{'productos':Producto.objects.order_by('folio')})

def producto_cambiar(request, folio):
    producto=Producto.objects.get(folio=folio)
    if request.method == 'GET':
        form=ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST,instance=producto)
        form.folio=producto.folio
        form.nombre=producto.nombre
        form.descripcion=producto.descripcion
        form.clasificacion=producto.clasificacion
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('productos_all')
    return render(request, 'admin/producto_form.html', {'form':form})

def ventas_totales(request):
    if esAdmin():
        form=Factura.objects.all();
        render(request,'admin/ventasTotales.html')

def ventas_parciales(request):
    if esAdmin():
        form=Factura.objects.all();
        render(request,'admin/ventasTotales.html')

def producto_eliminar(request,folio):
    producto=Producto.objects.get(folio=folio)
    if request.method=='POST':
        producto.delete()
        return redirect('productos_all')
    return render(request, 'admin/producto_eliminar.html', {'producto':producto})

def factura(request):
    factura=Factura.objects.all()
    contexto={'productos':factura}
    return render(request, 'admin/historial.html', contexto)

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['username']
            if Usuario.objects.filter(username=nombre).exists():
                messages.add_message(request, messages.INFO, 'El nombre de usuario ya existe')
            else:
                form.save()
                factura = Factura(usuario=Usuario.objects.get(username=nombre))
                factura.save()
                return redirect('inicio')
    else:
        form = UsuarioForm()
    return render(request, 'cliente/crearUsuario.html', {'form': form})

def anadir_carrito(request,Folio):
    global logeo
    producto=Producto.objects.get(folio=Folio)
    print(producto)
    if producto.cantidad>0 and logeo!=0:
        facturaza=Factura.objects.filter(usuario=Usuario.objects.get(username=logeo)).order_by('-id')[:1].get()
        producto2=ProductoIndividual(nombre=producto.nombre,provedor=producto.provedor,
        clasificacion=producto.clasificacion,precio=producto.precio,
        descuento=producto.descuento,factura=facturaza,total=producto.total)
        producto2.save()
        producto.cantidad=producto.cantidad-1
        producto.save()
    return redirect(productos)


def sesion(request):
    global logeo
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data['username']
            if Usuario.objects.filter(username=nombre).exists():
                contra=form.cleaned_data['password']
                if Usuario.objects.filter(password=contra).exists():
                    logeo=nombre
                    return redirect('inicio')
                else:
                    messages.add_message(request, messages.INFO, 'Contraseña incorrecta')
            else:
                messages.add_message(request, messages.INFO, 'Usuario Incorrecto')
    else:
        form = LoginForm()
    return render(request, 'cliente/login.html', {'form': form})

def administrador(request):
    return HttpResponse("Administrador")

def contacto(request):
    return render(request,'farmacia/contacto.html')

def promocion(request):
    return render(request,'farmacia/promociones.html')
