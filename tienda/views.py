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

# ----- Inicio de Sesion ----- #
def ver_inicio_sesion(request):
    return render(request, 'tienda/inicio_sesion.html')

# ------ Metodo cliente/portal ------ #
def agregar_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Cliente agregado exitosamente.')
            return redirect('inicio_sesion')
    else:
        form = ClienteForm()
        return render(request, 'tienda/cliente_form.html',
                      {
                        'form': form
                      })

# ---------- Catalogo productos ---------------------
def catalogo(request):
    """Retorna una lista de productos dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """
    busqueda = request.GET.get('busqueda')

    productos = Producto.objects.all()

    if busqueda != '' and busqueda is not None:
        productos = Producto.objects.filter(nombre__icontains=busqueda)

    for producto in productos:
        producto.precio_front = formatear_numero(producto.precio_normal)
        producto.poferta_front = formatear_numero(producto.precio_oferta)

    return render(request, 'tienda/productos.html',
                  {
                    'productos': productos
                  })


def detalle_producto(request, id):

    producto = Producto.objects.get(producto_id=id)

    producto.precio_front = formatear_numero(producto.precio_normal)
    producto.poferta_front = formatear_numero(producto.precio_oferta)

    return render(request, 'tienda/detalle_producto.html',
                  {
                    'producto': producto
                  })


def formatear_numero(entero):
    numero_formateado = f"{entero:,}"

    resultado = format(numero_formateado).replace(',', '.')

    return resultado


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
    edita_producto = True

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
                          'form': form,
                          'edita': edita_producto
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


# ----- Clientes ------
def ver_clientes_admin(request):
    run = Cliente.objects.all()

    return render(request, 'tienda/admin/usuarios/clientes.html',
                  {
                    'run': run
                  })


def agregar_clientes_admin(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Cliente agregado exitosamente.')
            return redirect('clientes_admin')
    else:
        form = ClienteForm()
        return render(request, 'tienda/admin/usuarios/cliente_admin_form.html',
                      {
                        'form': form
                      })


def obtener_clientes_admin(request):

    run = request.GET.get('run')
    appaterno= request.GET.get('appaterno')
    genero = request.GET.get('genero')
    cliente = Cliente.objects.all()

    # Busca tres campos
    if run != '' and appaterno != '' and genero != '':
        cliente = Cliente.objects.filter(run__icontains=run, appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo dos campos
    elif run != '' and appaterno != '':
        cliente = Cliente.objects.filter(run__icontains=run, appaterno__icontains=appaterno)
    elif run != '' and genero != '':
        cliente = Cliente.objects.filter(run__icontains=run, genero__icontains=genero)
    elif appaterno != '' and genero != '':
        cliente = Cliente.objects.filter(appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo un campo
    elif run != '':
        cliente = Cliente.objects.filter(run__icontains=run)
    elif appaterno != '':
        cliente = Cliente.objects.filter(appaterno__icontains=appaterno)
    elif genero != '':
        cliente = Cliente.objects.filter(genero__icontains=genero)

    return render(request, 'tienda/admin/usuarios/clientes.html',
                {
                'cliente': cliente
                })


def actualizar_clientes_admin(request, id):
    #logger.info('AAA')
    cliente = Cliente.objects.get(usuario_id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('clientes_admin')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'tienda/admin/usuarios/cliente_admin_form.html',
                      {
                          'form': form
                      })

# ----- Administrador ------
def ver_administrador_admin(request):
    run = Administrador.objects.all()

    return render(request, 'tienda/admin/usuarios/administrador.html',
                  {
                    'run': run
                  })


def agregar_administrador_admin(request):

    if request.method == 'POST':

        form = AdministradorForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Administrador agregado exitosamente.')
            return redirect('administrador_admin')
    else:
        form = AdministradorForm()
        return render(request, 'tienda/admin/usuarios/administrador_admin_form.html',
                      {
                        'form': form
                      })


def obtener_administrador_admin(request):

    run = request.GET.get('run')
    appaterno= request.GET.get('appaterno')
    genero = request.GET.get('genero')
    administrador = Administrador.objects.all()

    # Busca tres campos
    if run != '' and appaterno != '' and genero != '':
        administrador = Administrador.objects.filter(run__icontains=run, appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo dos campos
    elif run != '' and appaterno != '':
        administrador = Administrador.objects.filter(run__icontains=run, appaterno__icontains=appaterno)
    elif run != '' and genero != '':
        administrador = Administrador.objects.filter(run__icontains=run, genero__icontains=genero)
    elif appaterno != '' and genero != '':
        administrador = Administrador.objects.filter(appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo un campo
    elif run != '':
        administrador = Administrador.objects.filter(run__icontains=run)
    elif appaterno != '':
        administrador = Administrador.objects.filter(appaterno__icontains=appaterno)
    elif genero != '':
        administrador = Administrador.objects.filter(genero__icontains=genero)


    return render(request, 'tienda/admin/usuarios/administrador.html',
                {
                'administrador': administrador
                })


def actualizar_administrador_admin(request, id):

    administrador = Administrador.objects.get(usuario_id=id)
    if request.method == "POST":
        form = AdministradorForm(request.POST, instance=administrador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador actualizado exitosamente.')
            return redirect('administrador_admin')
    else:
        form = AdministradorForm(instance=administrador)
        return render(request, 'tienda/admin/usuarios/administrador_admin_form.html',
                      {
                          'form': form
                      })


def eliminar_administrador_admin(request, id):
    administrador = Administrador.objects.get(usuario_id=id)

    if request.method == 'POST':
        administrador.delete()
        messages.success(request, 'Administrador eliminado exitosamente.')
        return redirect('administrador_admin')

    return render(request, 'tienda/admin/usuarios/eliminar_administrador.html',
                  {
                      'administrador': administrador
                  })


# ----- Empleado ------
def ver_empleado_admin(request):
    run = Empleado.objects.all()

    return render(request, 'tienda/admin/usuarios/empleado.html',
                  {
                    'run': run
                  })


def agregar_empleado_admin(request):

    if request.method == 'POST':

        form = EmpleadoForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Empleado agregado exitosamente.')
            return redirect('empleado_admin')
    else:
        form = EmpleadoForm()
        return render(request, 'tienda/admin/usuarios/empleado_admin_form.html',
                      {
                        'form': form
                      })


def obtener_empleado_admin(request):

    run = request.GET.get('run')
    appaterno= request.GET.get('appaterno')
    genero = request.GET.get('genero')
    empleado = Empleado.objects.all()

    # Busca tres campos
    if run != '' and appaterno != '' and genero != '':
        empleado = Empleado.objects.filter(run__icontains=run, appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo dos campos
    elif run != '' and appaterno != '':
        empleado = Empleado.objects.filter(run__icontains=run, appaterno__icontains=appaterno)
    elif run != '' and genero != '':
        empleado = Empleado.objects.filter(run__icontains=run, genero__icontains=genero)
    elif appaterno != '' and genero != '':
        empleado = Empleado.objects.filter(appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo un campo
    elif run != '':
        empleado = Empleado.objects.filter(run__icontains=run)
    elif appaterno != '':
        empleado = Empleado.objects.filter(appaterno__icontains=appaterno)
    elif genero != '':
        empleado = Empleado.objects.filter(genero__icontains=genero)


    return render(request, 'tienda/admin/usuarios/empleado.html',
                {
                'empleado': empleado
                })


def actualizar_empleado_admin(request, id):

    empleado = Empleado.objects.get(usuario_id=id)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('empleado_admin')
    else:
        form = EmpleadoForm(instance=empleado)
        return render(request, 'tienda/admin/usuarios/empleado_admin_form.html',
                      {
                          'form': form
                      })




# ----- Vendedor ------
def ver_vendedor_admin(request):
    run = Vendedor.objects.all()

    return render(request, 'tienda/admin/usuarios/vendedor.html',
                  {
                    'run': run
                  })


def agregar_vendedor_admin(request):

    if request.method == 'POST':

        form = VendedorForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Vendedor agregado exitosamente.')
            return redirect('vendedor_admin')
    else:
        form = VendedorForm()
        return render(request, 'tienda/admin/usuarios/vendedor_admin_form.html',
                      {
                        'form': form
                      })


def obtener_vendedor_admin(request):

    run = request.GET.get('run')
    appaterno= request.GET.get('appaterno')
    genero = request.GET.get('genero')
    vendedor = Vendedor.objects.all()

    # Busca tres campos
    if run != '' and appaterno != '' and genero != '':
        vendedor = Vendedor.objects.filter(run__icontains=run, appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo dos campos
    elif run != '' and appaterno != '':
        vendedor = Vendedor.objects.filter(run__icontains=run, appaterno__icontains=appaterno)
    elif run != '' and genero != '':
        vendedor = Vendedor.objects.filter(run__icontains=run, genero__icontains=genero)
    elif appaterno != '' and genero != '':
        vendedor = Vendedor.objects.filter(appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo un campo
    elif run != '':
        vendedor = Vendedor.objects.filter(run__icontains=run)
    elif appaterno != '':
        vendedor = Vendedor.objects.filter(appaterno__icontains=appaterno)
    elif genero != '':
        vendedor = Vendedor.objects.filter(genero__icontains=genero)


    return render(request, 'tienda/admin/usuarios/vendedor.html',
                {
                'vendedor': vendedor
                })


def actualizar_vendedor_admin(request, id):

    vendedor = Vendedor.objects.get(usuario_id=id)
    if request.method == "POST":
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendedor actualizado exitosamente.')
            return redirect('vendedor_admin')
    else:
        form = VendedorForm(instance=vendedor)
        return render(request, 'tienda/admin/usuarios/vendedor_admin_form.html',
                      {
                          'form': form
                      })

# ------------------ Ordenes de Compra ------------------

def administrar_oc(request):
    """Muestra la página de gestión de ordenes de compra.

    Args:
    Returns:
        Una página
    """
    query = Query().from_table('ordendecompra')
    ocs = query.select()

    return render(request, 'tienda/admin/ordenes_compra/ordenes_compra.html',
                {
                    'clase_administrada': 'orden_de_compra',
                    'coleccion': ocs
                })


def actualizar_orden(request, id):
    """Actualiza un orden segun su id

    Args:
        id (int): id del orden a modificar
    Returns:
        Una página
    """
    edita_orden = True

    orden = ordendecompra.objects.get(id=id)
    if request.method == "POST":
        form = ordenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            messages.success(request, 'orden actualizado exitosamente.')
            return redirect('ordenes_admin')
    else:
        form = ordenForm(instance=orden)
        return render(request, 'tienda/admin/ordenes/orden_form.html',
                      {
                          'form': form,
                          'edita': edita_orden
                      })