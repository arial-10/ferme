from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from querybuilder.query import Query


def home(request):
    return render(request, 'tienda/home.html')



def home_admin(request):
    return render(request, 'tienda/admin/home.html')


def ver_productos_admin(request):

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'marcas': obtener_marcas()
                  })

def obtener_productos_admin(request):

    nombre = request.GET.get('nombre')
    id_marca = request.GET.get('marca')
    sku = request.GET.get('sku')
    productos = Producto.objects.all()

    if nombre != '' and sku == '' and id_marca == '0':
        productos = Producto.objects.filter(nombre__icontains=nombre)
    if nombre == '' and sku != '' and id_marca == '0':
        productos = Producto.objects.filter(sku__contains=sku)
    if nombre == '' and sku == '' and id_marca != '0':
        productos = Producto.objects.filter(marca=id_marca)

    if nombre != '' and sku != '' and id_marca == '0':
        productos = Producto.objects.filter(nombre__icontains=nombre,
                                            sku__contains=sku)
    if nombre != '' and sku == '' and id_marca != '0':
        productos = Producto.objects.filter(nombre__icontains=nombre,
                                            marca=id_marca)
    if nombre == '' and sku != '' and id_marca != '0':
        productos = Producto.objects.filter(sku__contains=sku,
                                            marca=id_marca)

    if nombre != '' and sku != '' and id_marca != '0':
        productos = Producto.objects.filter(nombre__icontains=nombre,
                                            sku__contains=sku,
                                            marca=id_marca)

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'productos': productos,
                    'marcas': obtener_marcas()
                  })


def agregar_producto(request):

    if request.method == 'POST':

        form = ProductoForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.url_img = 'img/producto/' + model_instance.producto_id + '.jpg'
            model_instance.save()
            messages.success(request, 'Producto agregado exitosamente.')

            return redirect('productos_admin')
    else:
        form = ProductoForm()
        return render(request, 'tienda/admin/productos/producto_form.html',
                      {
                        'form': form
                      })

def actualizar_producto(request, id):
    """Actualiza un producto segun su id

    Args:
        request: esto no es necesario pero lo puse pa que se entienda
        id (int): id del producto a modificar
    Returns:
        Una página
    """
    producto = Producto.objects.get(producto_id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('productos_admin')
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'tienda/admin/productos/producto_form.html',
                      {
                          'form': form
                      })


def eliminar_producto(request, id):
    producto = Producto.objects.get(producto_id=id)

    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('productos_admin')

    return render(request, 'tienda/admin/productos/eliminar_producto.html',
                  {
                      'producto': producto
                  })


def obtener_marcas():
    marcas = Marca.objects.all()

    return marcas


def cancelar_producto(request):
    return redirect(reverse('productos_admin'))



def home_empleado(request):
    return render(request, 'tienda/empleado/home.html')
