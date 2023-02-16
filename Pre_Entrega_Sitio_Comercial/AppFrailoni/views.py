from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppFrailoni.forms import *


# Create your views here.

def inicio(request):
    return render (request, "inicio.html")


def producto(request):
    if request.method== "POST":
        form=ProductoForms (request.POST)
        if form.is_valid():
            infoprod= form.cleaned_data
            nombreprod= infoprod["nombreprod"]
            caracteristicas= infoprod["caracteristicas"]
            precio= infoprod["precio"]
            formuprod=Producto( nombreprod=nombreprod, caracteristicas=caracteristicas, precio=precio)
            formuprod.save()        
            return render (request, "inicio.html", {"mensaje1": "Tu información sobre el producto ha sido enviada. A la brevedad nos comunicaremos y la tendremos en cuenta para diseñar tu producto."})
        else :
            return render (request, "producto.html", {"form": form, "mensaje1": "Información no valida. Completo erroneamente el fomulario de PRODUCTO"})
    else:
        infoprod1= ProductoForms()
        return render (request, "producto.html", {"form": infoprod1 })
    
    
def proveedores(request):
    if request.method== "POST":
        form=ProveedoresForms (request.POST)
        if form.is_valid():
            info4= form.cleaned_data
            nombreproveedor= info4["nombreproveedor"]
            productoproveedor= info4["productoproveedor"]
            precio= info4["precio"]
            formuproveedor= Proveedores( nombreproveedor=nombreproveedor, productoproveedor=productoproveedor, precio=precio)
            formuproveedor.save()        
            return render (request, "inicio.html", {"mensaje3": "Tu información ha sido enviada. A la brevedad, nos contactaremos para que seas nuestro futuro proveedor si cumples con nuestras condiciones..."})
        else :
            return render (request, "proveedores.html", {"form": form, "mensaje3": "Información no valida. Completo erroneamente el fomulario de PROVEEDORES"})
    else:
        info3= ProveedoresForms()
        return render (request, "proveedores.html", {"form": info3 })

    
def cliente(request):
    if request.method== "POST":
        form=ClienteForms (request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            correo= info["correo"]
            numerocel= info["numerocel"]
            formucliente=Cliente( nombre=nombre, correo=correo, numerocel=numerocel)
            formucliente.save()        
            return render (request, "inicio.html", {"mensaje": "Tu información ha sido enviada. A la brevedad, nos contactaremos."})
        else :
            return render (request, "cliente.html", {"form": form, "mensaje": "Información no valida. Completo erroneamente el fomulario de CLIENTES"})
    else:
        info1= ClienteForms()
        return render (request, "cliente.html", {"form": info1 })






def busquedadedatos(request):
    return render (request, "busquedadedatos.html")


def busqueda(request):

    precio= request.GET["precio"]
    if precio != "":
        precios=Producto.objects.filter(precio=precio)
        return render (request, "resultado.html", {"precios":precios})
        
    else:
     return render (request, "busquedadedatos.html", {"mensaje": "Datos incorrecto"})


