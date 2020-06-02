from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *


def home(request):
    return render(request, 'tienda/home.html')


# ================ Metodos Ferme Admin ====================================
def home_admin(request):
    return render(request, 'tienda/admin/home.html')

# =============== Seccion Producto ======================================
def ver_productos_admin(request):
    return render(request, 'tienda/admin/productos/productos.html')


def obtener_productos_admin(request):

    nombre = request.GET.get('nombre')
    id_marca= request.GET.get('marca')
    sku = request.GET.get('sku')
    productos = Producto.objects.all();

    if nombre != '' and sku == '':
        productos = Producto.objects.filter(nombre__icontains=nombre)
    if nombre == '' and sku != '':
        productos = Producto.objects.filter(sku__contains=sku)
    if nombre != '' and sku != '':
        productos = Producto.objects.filter(nombre__icontains=nombre, sku__contains=sku)

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'productos': productos
                  })


def abrir_form_producto(request):
    abrir_form = True

    return render(request, 'tienda/admin/productos/productos.html',
            {
                'abrir_form': abrir_form
            })
