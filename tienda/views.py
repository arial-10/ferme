from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from querybuilder.query import Query

# ======================== FERME TIENDA ========================
def home(request):
    return render(request, 'tienda/home.html')

# ======================== FERME ADMIN ========================
def home_admin(request):
    return render(request, 'tienda/admin/home.html')

# ------------ PRODUCTOS ------------
def ver_productos_admin(request):
    """Muestra la página de gestión de Productos.

    Args:

    Returns:
        Una página
    """

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'marcas': obtener_marcas()
                  })

def obtener_productos_admin(request):
    """Retorna una lista de productos dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """

    nombre = request.GET.get('nombre')
    id_marca = request.GET.get('marca')
    sku = request.GET.get('sku')
    # productos = Producto.objects.all()
    nombre_marca = []

    query = Query().from_table(Producto)

    if nombre != '':
        query = query.where(nombre__contains=nombre)
    if sku != '':
        query = query.where(sku__contains=sku)
    if id_marca != '0':
        # Traemos los registros
        query = query.where(marca_id=id_marca)
        # Luego, buscamos el nombre de la marca
        query2 = Query().from_table(Marca, ['NOMBRE']).where(id=id_marca)
        # Guardamos el nombre
        nombre_marca = query2.select()


    productos = query.select()

    # Si encontro el nombre
    if len(nombre_marca) > 0:
        # Le pasamos a todos los productos(diccionarios) el nombre de la marca
        for producto in productos:
            producto['NOMBRE_MARCA'] = nombre_marca[0]['NOMBRE']


    # if nombre != '' and sku == '' and id_marca == '0':
    #     productos = Producto.objects.filter(nombre__icontains=nombre)
    # if nombre == '' and sku != '' and id_marca == '0':
    #     productos = Producto.objects.filter(sku__contains=sku)
    # if nombre == '' and sku == '' and id_marca != '0':
    #     productos = Producto.objects.filter(marca=id_marca)

    # if nombre != '' and sku != '' and id_marca == '0':
    #     productos = Producto.objects.filter(nombre__icontains=nombre,
    #                                         sku__contains=sku)
    # if nombre != '' and sku == '' and id_marca != '0':
    #     productos = Producto.objects.filter(nombre__icontains=nombre,
    #                                         marca=id_marca)
    # if nombre == '' and sku != '' and id_marca != '0':
    #     productos = Producto.objects.filter(sku__contains=sku,
    #                                         marca=id_marca)

    # if nombre != '' and sku != '' and id_marca != '0':
    #     productos = Producto.objects.filter(nombre__icontains=nombre,
    #                                         sku__contains=sku,
    #                                         marca=id_marca)

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'productos': productos,
                    'marcas': obtener_marcas()
                  })


def agregar_producto(request):
    """Agrega un producto a la base de datos

    Args:

    Returns:
        Una página
    """

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
    """Actualiza un producto segun su id

    Args:
        id (int): id del producto a eliminar
    Returns:
        Una página
    """

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
    """Obtiene todos los registros de la tabla Marca

    Args:

    Returns:
        marcas: Queryset con las marcas
    """

    marcas = Marca.objects.all()

    return marcas


def cancelar_producto(request):
    """Redirige a la página principal del módulo Productos.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('productos_admin'))



def home_empleado(request):
    return render(request, 'tienda/empleado/home.html')
