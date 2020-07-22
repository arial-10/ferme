from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from django.forms import modelformset_factory
from .models import *
from .forms import *
from querybuilder.query import Query
from . import utils
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import *
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import timedelta

# ======================== FERME TIENDA ========================
def home(request):
    return render(request, 'tienda/home.html')

# ----- Inicio de Sesion ----- #
def ver_inicio_sesion(request):
    return render(request, 'tienda/inicio_sesion.html')

def ver_inicio_sesion_admin(request):
    return render(request, 'tienda/admin/inicio_sesion_admin.html')


# Iniciar sesión
def cliente_login(request):
    # Si estoy recibiendo un formulario con method POST
    if request.method == 'POST':
        # Recibimos la información del formulario
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        origen = request.POST.get('origen')
        print(origen)
        if origen == '1':
            # Autenticamos al usuario
            user = Cliente.objects.filter(email=email, contrasena=contrasena).exists()
            print(user)
            # Verificamos que exista el usuario
            if user:
                # Verificamos si está activo
                if user == True:
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Tu cuenta está inactiva.")
            else:  # Si no existe el usuario
                print("email: {} - contrasena: {}".format(email, contrasena))
                return render(request, 'tienda/inicio_sesion.html', {})

        if origen == '2': #Vengo del administrador
            # Autenticamos al usuario
            user = Administrador.objects.filter(email=email, contrasena=contrasena).exists()
            print(user)
            # Verificamos que exista el usuario
            if user:
                # Verificamos si está activo
                if user == True:
                    return HttpResponseRedirect('/ferme-admin')
                else:
                    return HttpResponse("Tu cuenta está inactiva.")
            else:  # Si no existe el usuario
                print("email: {} - contrasena: {}".format(email, contrasena))
                return render(request, 'tienda/admin/inicio_sesion_admin.html', {})


# Recuperar contraseña
def recuperar_contrasena_cliente(request):
    # create message object instance
    if request.method == 'POST':
        msg = MIMEMultipart()

        email = request.POST.get('email')
        cliente = Cliente.objects.get(email=email)

        message = "Hola " + cliente.nombres + ",\n" + "Has solicitado recuperar tu contraseña de acceso a FerreteriaFerme.com\n\n" + "Usa tu contraseña para poder iniciar sesión y realizar tus compras: " + "\n\n" + cliente.contrasena


        # setup the parameters of the message
        password = "ferreferme"
        msg['From'] = "ferreteriasferme@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Recuperación de Contraseña"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        #create server
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)


        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        return render(request, 'tienda/inicio_sesion.html')

    else:
        return render(request, 'tienda/recuperar_contrasena.html')


def recuperar_contrasena_admin(request):
    # create message object instance
    if request.method == 'POST':
        msg = MIMEMultipart()

        email = request.POST.get('email')
        administrador = Administrador.objects.get(email=email)

        message = "Hola " + administrador.nombres + ",\n" + "Has solicitado recuperar tu contraseña de acceso a FerreteriaFerme.com\n\n" + "Usa tu contraseña para poder iniciar sesión y realizar tus compras: " + "\n\n" + administrador.contrasena


        # setup the parameters of the message
        password = "ferreferme"
        msg['From'] = "ferreteriasferme@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Recuperación de Contraseña"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        #create server
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)


        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        return render(request, 'tienda/admin/inicio_sesion_admin.html')

    else:
        return render(request, 'tienda/admin/recuperar_contrasena_admin.html')

def calcular_total(carro_id):
    productos = CarroProducto.objects.filter(carro=carro_id)
    total = 0
    for producto in productos:
        total += precioAsInt(producto.precio)
    return total

def tipo_despacho(request, carro, seleccion_despacho=''):
    # Generadas en el código porque el manejo de estas fechas
    # Está fuera del scope del sistema
    # son tuplas en la forma (fecha, precio)
    fechas_retiro = [
        (generar_fecha(0), 0),
        (generar_fecha(3), 0),
        (generar_fecha(6), 0)
    ]

    fechas_envio = [
        (generar_fecha(1), 2990),
        (generar_fecha(4), 1990),
        (generar_fecha(7), 1990)
    ]

    #Este es el carro de compras
    carro_cliente = Carro.objects.get(carro_id=carro)
    usuario = carro_cliente.cliente
    cliente = Cliente.objects.get(nombre_usuario=usuario.username)
    vendedor = Vendedor.objects.get(nombre_usuario='tienda_virtual')

    # Si estoy recibiendo un formulario con method POST
    if request.method == 'POST':
        if seleccion_despacho != '':
            despachoForm = DespachoForm(request.POST)
            retiroForm = RetiroForm(request.POST)
            print(despachoForm.errors)
            if seleccion_despacho == 'envio' and despachoForm is not None:
                if despachoForm.is_valid():
                    compra = Compra.objects.create(
                            vendedor = Vendedor.objects.get(nombre_usuario='tienda_virtual'),
                            monto_total = calcular_total(carro),
                            cliente = cliente
                        )
                    despacho = despachoForm.save(commit=False)
                    despacho.compra = compra
                    despacho.save()
                    for producto in CarroProducto.objects.filter(carro=carro_cliente.carro_id):
                        ProductoCompra.objects.create(
                                compra = compra,
                                producto = producto.producto,
                                cantidad = producto.cantidad
                            )
                    return redirect( 'pago', despacho=despacho.id)
            elif seleccion_despacho == 'retiro' and retiroForm is not None:
                if retiroForm.is_valid():
                    retiroForm.save()
                    return render(request, 'tienda/pago.html',{
                            'despacho': retiroForm.instance
                        })
            else:
                compra.delete()
            
            despachoForm = DespachoForm({
                    'rut_receptor': cliente.run,
                    'direccion': cliente.direccion,
                    'telefono_contacto': cliente.telefono
                })
            retiroForm = RetiroForm({
                    'rut_receptor': cliente.run,
                    'empleado': 1
                })
            return render(request, 'tienda/tipo_despacho.html',
                        {
                            'fechas_retiro': fechas_retiro,
                            'fechas_envio': fechas_envio,
                            'carro': carro,
                            'usuario': usuario,
                            'form_despacho': despachoForm,
                            'form_retiro': retiroForm
                        })
        else:
            seleccion_despacho = ''
            despachoForm = DespachoForm({
                    'rut_receptor': cliente.run,
                    'direccion': cliente.direccion,
                    'telefono_contacto': cliente.telefono
                })
            retiroForm = RetiroForm({
                    'rut_receptor': cliente.run,
                    'empleado': 1
                })
            return render(request, 'tienda/tipo_despacho.html',
                        {
                            'fechas_retiro': fechas_retiro,
                            'fechas_envio': fechas_envio,
                            'carro': carro,
                            'usuario': usuario,
                            'form_despacho': despachoForm,
                            'form_retiro': retiroForm,
                            'seleccion_despacho': seleccion_despacho
                        })
    else:
        despachoForm = DespachoForm({
                'rut_receptor': cliente.run,
                'direccion': cliente.direccion,
                'telefono_contacto': cliente.telefono
            })
        retiroForm = RetiroForm({
                'rut_receptor': cliente.run,
                'empleado': 1
            })
        seleccion_despacho = ''
        return render(request, 'tienda/tipo_despacho.html',
                    {
                        'fechas_retiro': fechas_retiro,
                        'fechas_envio': fechas_envio,
                        'carro': carro,
                        'usuario': usuario,
                        'form_despacho': despachoForm,
                        'form_retiro': retiroForm,
                        'seleccion_despacho': seleccion_despacho
                    })

def pago(request, despacho=''):

    despacho = DespachoDomicilio.objects.get(id=despacho)
    compra = Compra.objects.get(id_compra=despacho.compra.id_compra)
    items = ProductoCompra.objects.filter(compra=compra.id_compra)
    
    if request.method == 'POST':
        print(request.POST)
        forma_pago = request.POST.get('radiosPago')
        boleta = Boleta.objects.create(
                sucursal='tienda virtual',
                direccion=despacho.direccion,
                comuna=despacho.comuna,
                fecha_compra=datetime.now(),
                terminal=0,
                tipo_pago=forma_pago,
                anulada='no',
                compra = compra,
                rut_persona = compra.cliente.run
            )
        return redirect('/')
    else:
        return render(request, 'tienda/pago.html', {
                'despacho': despacho,
                'compra': compra,
                'items': items
            })


def ver_mis_ordenes(request):
    request.user
    usuario = request.user
    cliente = Cliente.objects.get(user=usuario)

    fechaDespachoManana = 1
    now = datetime.now()
    new_date = now + timedelta(days=1)
    formatoFechaDespacho = new_date.strftime('%d/%m/%Y')   
    fechaDespachoManana = formatoFechaDespacho

    new_date = now + timedelta(days=4)
    formatoFechaDespachoL2 = new_date.strftime('%d/%m/%Y')   
    fechaDespachoL2 = formatoFechaDespachoL2

    numOrden= now.strftime('%m%y%I%M%S') 
    numDespacho= now.strftime('%H%m%I%M%H') 
    
    try:
        compra = Compra.objects.filter(cliente_id = cliente.usuario_id).first()
    except Exception as e:
        print(e)
        messages.error(request, 'Aun no tienes ordenes pendientes')
        return redirect('home')
    compra_id = compra.id_compra
    monto_total = compra.monto_total

    productoCompra = ProductoCompra.objects.get(compra_id = compra_id)
    producto_id = productoCompra.producto_id
    cantidad = productoCompra.cantidad

    producto = Producto.objects.get(producto_id = producto_id)
    url_img = producto.url_img
    nombre = producto.nombre
    descripcion = producto.descripcion

    return render(request, 'tienda/mis_ordenes.html',
        {
        'fechaDespachoManana': formatoFechaDespacho,
        'fechaDespachoL2': formatoFechaDespachoL2,
        'numOrden': numOrden,
        'numDespacho': numDespacho,
        'productoId': producto_id,
        'urlImg': url_img,
        'nombre': nombre,
        'monto_total': monto_total,
        'descripcion': descripcion,
        'cantidad': cantidad
        })

# ======================== FERME EMPLEADO ========================
def home_empleado(request):
    return render(request, 'tienda/home_empleado.html')

def ver_boleta(request):
    """Muestra la página de gestión de Clientes.

    Args:

    Returns:
        Una página
    """
    documento_id = Boleta.objects.all()

    return render(request, 'tienda/emp_boletas.html',
                  {
                    'documento_id': documento_id
                  })    
                

def obtener_boleta(request):
    """Retorna la boleta respecto a los datos ingresados 

    Args:

    Returns:
        Una página
    """
    documento_id = request.GET.get('documento_id')    
    query = Query().from_table(Boleta)

    if documento_id != '':
        query = query.where(documento_id=documento_id)

    boletas = query.select()

    return render(request, 'tienda/emp_boletas.html',
                {
                'boletas': boletas
                })


def nota_credito(request, id):
    query = Query().from_table(Boleta)
    query = query.where(documento_id=id)
    boletas = query.select()

    return render(request, 'tienda/nota_credito.html',
                    {
                        'boletas': boleta
                    })


def agregar_notaCredito(request):
    now = datetime.now()
    id = now.strftime('%m%y%I%M%S') 
    sucursal = request.POST.get('sucursal')
    direccion = request.POST.get('direccion')
    comuna = request.POST.get('comuna')
    fecha_compra = request.POST.get('fecha_compra')
    terminal = request.POST.get('terminal')
    tipo_pago = request.POST.get('tipo_pago')
    estado = request.POST.get('estado')
    fecha_anulacion = request.POST.get('fecha_anulacion')
    doc_asociado = request.POST.get('doc_asociado')
    desc_motivo = request.POST.get('desc_motivo')
    compra_id = request.POST.get('compra_id')
    empleado_id = request.POST.get('empleado_id')

    if request.method == 'POST':

        notaCredito = NotaCredito()
        notaCredito.id = id
        notaCredito.sucursal = sucursal
        notaCredito.direccion = direccion
        notaCredito.comuna = comuna
        notaCredito.fecha_compra = fecha_compra
        notaCredito.terminal = terminal
        notaCredito.tipo_pago = tipo_pago
        notaCredito.estado = estado
        notaCredito.fecha_anulacion = fecha_anulacion
        notaCredito.doc_asociado = doc_asociado
        notaCredito.desc_motivo = desc_motivo
        notaCredito.compra_id = compra_id
        notaCredito.empleado_id = empleado_id
        notaCredito.save()

        messages.success(request, 'Nota de credito creada exitosamente.')

    return render(request, 'tienda/emp_boletas.html')


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
    cantidad_productos = 0

    marcas = Marca.objects.all()
    productos = Producto.objects.all()

    if busqueda != '' and busqueda is not None:
        productos = Producto.objects.filter(nombre__icontains=busqueda)

    for producto in productos:
        producto.precio_front = utils.formatear_numero_miles(
            producto.precio_normal)
        producto.poferta_front = utils.formatear_numero_miles(
            producto.precio_oferta)

    cantidad_productos = len(productos)

    return render(request, 'tienda/productos.html',
                  {
                    'productos': productos,
                    'marcas': marcas,
                    'cantidad': cantidad_productos
                  })


def detalle_producto(request, id):
    """Retorna un producto que coincida con el id ingresado

    Args:

    Returns:
        Una página
        producto: Queryset del producto
    """
    producto = Producto.objects.get(producto_id=id)

    producto.precio_front = utils.formatear_numero_miles(
        producto.precio_normal)
    producto.poferta_front = utils.formatear_numero_miles(
        producto.precio_oferta)

    return render(request, 'tienda/detalle_producto.html',
                  {
                    'producto': producto
                  })


def filtrar_catalogo(request):
    """Retorna una lista de productos dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """
    productos = []
    marcas = Marca.objects.all()
    marcas_seleccionadas = []
    precios = {
        'precio1': '5000',
        'precio2': '25000',
        'precio3': '50000',
        'precio4': '100000',
        'precio5': '200000'
    }
    precios_seleccionados = []
    cantidad_productos = 0

    for marca in marcas: 
        # Validamos que el parametro por GET exista
        if request.GET.get(marca.nombre) is not None:
            marca_id = int(request.GET.get(marca.nombre))
            if marca.id == marca_id:
                marcas_seleccionadas.append(Marca.objects.get(id=marca.id))
    # Validamos los precios que se seleccionaron en el front
    for key, value in precios.items():
        if request.GET.get(key) is not None:
            precio_int = int(value)
            precios_seleccionados.append(precio_int)

    precios_seleccionados.sort()

    # Distintos escenarios
    # Se selecciona solo marcas    
    if len(marcas_seleccionadas) > 0 and len(precios_seleccionados) == 0:
        for marca_seleccionada in marcas_seleccionadas:
            productos += Producto.objects.filter(marca=marca_seleccionada.id)
    # Se selecciona solo precios
    if len(precios_seleccionados) > 0 and len(marcas_seleccionadas) == 0:
        if len(precios_seleccionados) == 1:
            if precios_seleccionados[0] == 5000:
                productos = Producto.objects.filter(precio_normal__lte=5000)
            if precios_seleccionados[0] == 25000:
                productos = Producto.objects.filter(precio_normal__gt=5000,
                    precio_normal__lte=25000)
            if precios_seleccionados[0] == 50000:
                productos = Producto.objects.filter(precio_normal__gt=25000,
                    precio_normal__lte=50000)
            if precios_seleccionados[0] == 100000:
                productos = Producto.objects.filter(precio_normal__gt=50000,
                    precio_normal__lte=100000)
            if precios_seleccionados[0] == 200000:
                productos = Producto.objects.filter(precio_normal__gt=100000)
        else:
            if precios_seleccionados[0] == 5000:
                productos = Producto.objects.filter(precio_normal__gt=0,
                    precio_normal__lte=precios_seleccionados[
                        len(precios_seleccionados) - 1])
            elif precios_seleccionados[0] == 25000:
                productos = Producto.objects.filter(precio_normal__gt=5000,
                    precio_normal__lte=precios_seleccionados[
                        len(precios_seleccionados) - 1])
            elif precios_seleccionados[0] == 50000:
                productos = Producto.objects.filter(precio_normal__gt=25000,
                    precio_normal__lte=precios_seleccionados[
                        len(precios_seleccionados) - 1])
            else:
                productos = Producto.objects.filter(
                    precio_normal__gt=precios_seleccionados[0],
                    precio_normal__lte=precios_seleccionados[
                        len(precios_seleccionados) - 1])
    # Se seleccionan ambos
    if len(precios_seleccionados) > 0 and len(marcas_seleccionadas) > 0:
        for marca_seleccionada in marcas_seleccionadas:
            if len(precios_seleccionados) == 1:
                if precios_seleccionados[0]  == 5000:
                    productos += Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__lte=5000)
                if precios_seleccionados[0] == 25000:
                    productos += Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=5000,
                        precio_normal__lte=25000)
                if precios_seleccionados[0] == 50000:
                    productos += Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=25000,
                        precio_normal__lte=50000)
                if precios_seleccionados[0] == 100000:
                    productos += Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=50000,
                        precio_normal__lte=100000)
                if precios_seleccionados[0] == 200000:
                    productos += Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=100000)
            else:
                if precios_seleccionados[0] == 5000:
                    productos = Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=0,
                        precio_normal__lte=precios_seleccionados[
                            len(precios_seleccionados) - 1])
                elif precios_seleccionados[0] == 25000:
                    productos = Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=5000,
                        precio_normal__lte=precios_seleccionados[
                            len(precios_seleccionados) - 1])
                elif precios_seleccionados[0] == 50000:
                    productos = Producto.objects.filter(
                        marca=marca_seleccionada.id, precio_normal__gt=25000,
                        precio_normal__lte=precios_seleccionados[
                            len(precios_seleccionados) - 1])
                else:
                    productos = Producto.objects.filter(
                        marca=marca_seleccionada.id,
                        precio_normal__gt=precios_seleccionados[0],
                        precio_normal__lte=precios_seleccionados[
                            len(precios_seleccionados) - 1])

    if len(precios_seleccionados) == 0 and len(marcas_seleccionadas) == 0:
        productos = Producto.objects.all()

    for producto in productos:
        producto.precio_front = utils.formatear_numero_miles(
            producto.precio_normal)
        producto.poferta_front = utils.formatear_numero_miles(
            producto.precio_oferta)

    cantidad_productos = len(productos)

    return render(request, 'tienda/productos.html',
                  {
                    'productos': productos,
                    'marcas': marcas,
                    'marcas_selecc': marcas_seleccionadas,
                    'cantidad': cantidad_productos
                  })


def ver_categoria(request, id):
    """Retorna una lista de productos dependiendo de la categoria
    seleccionada

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """
    categoria = Categoria.objects.get(id=id)
    productos_categoria = CategoriaProducto.objects.filter(categoria=categoria.id)
    marcas = Marca.objects.all()
    productos = []
    aux = None;

    for producto in productos_categoria:
        aux = Producto.objects.get(producto_id=producto.producto.producto_id)
        productos.append(aux)
    
    cantidad = len(productos)

    return render(request, 'tienda/productos.html', {
            'productos': productos,
            'cantidad': cantidad,
            'marcas': marcas,
            'categoria': categoria
        })

# ---------- Carro de Compras ---------------------
def ver_carro(request):
    """Retorna una lista de productos que corresponden
     a los que estan en el carro de compras del usuario

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """
    if request.method == 'POST':
        carro_usuario = Carro.objects.get(cliente=request.user)
        return render(request, 'tienda/tipo_despacho.html', {
                'carro': carro_usuario.carro_id
            })
    else:
        carro = Carro.objects.get(cliente=request.user)
        productos_carro = []
        if carro is not None:
            productos_carro = CarroProducto.objects.filter(carro=carro)
        cantidad = len(productos_carro)
        return render(request, 'tienda/carro_compras.html', 
            {
                'productos': productos_carro,
                'cantidad': cantidad,
                'carro': carro
            })


def agregar_carro(request, id):
    """Agrega un producto al carro de compras.

    Args:

    Returns:
        Una página
    """
    if request.user.is_authenticated:
        usuario = request.user
        producto = Producto.objects.get(producto_id=id)
        cantidad = int(request.GET.get('cantidad'))
        carro = Carro.objects.get(cliente=usuario.id)
        precio = utils.formatear_numero_miles(producto.precio_normal * cantidad)
        carro_producto = CarroProducto.objects.create(cantidad=cantidad, producto=producto, carro=carro, precio=precio)
        messages.success(request, "Producto agregado correctamente al carrito de compras.")
    else:
        messages.error(request, "Antes de empezar a comprar, tiene que iniciar sesión.")

        
    return redirect(reverse('catalogo'))


def eliminar_carro(request, id):
    """Elimina un producto del carro de compras.

    Args:

    Returns:
        Una página
    """
    producto = CarroProducto.objects.get(id=id)
    producto.delete()
    messages.success(request, f"{producto} fue eliminado de tu carro de compras.")
    return redirect(reverse('carro'))

# ======================== FERME ADMIN ========================
@login_required(login_url='login_admin')
@solo_admin
def home_admin(request):
    es_admin = False
    es_vendedor = False
    es_empleado = False
    rol = ''

    user = request.user
    usuario = Administrador.objects.filter(user=user).first()

    if usuario is not None:
        es_admin = True
        rol = 'Administrador'
    if es_admin is False:
        usuario = Empleado.objects.filter(user=user).first()

        if usuario is not None:
            rol = 'Empleado'
            es_empleado = True
    if es_admin is False and es_empleado is False:
        usuario = Vendedor.objects.filter(user=user).first()
        
        if usuario is not None:
            rol = 'Vendedor'
            es_vendedor = True

    return render(request, 'tienda/admin/home.html', 
        {
            'usuario': usuario,
            'rol': rol
        })

# ------------ PRODUCTOS ------------
@login_required(login_url='login_admin')
def ver_productos_admin(request):
    """Muestra la página de gestión de Productos.

    Args:

    Returns:
        Una página
    """

    productos = Query().from_table(Producto).select()

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'marcas': obtener_marcas(),
                    'productos': productos
                  })

@login_required(login_url='login_admin')
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
    nombre_marca = []

    query = Query().from_table(Producto)

    if nombre != '':
        query = query.where(nombre__contains=nombre)
    if sku != '':
        query = query.where(sku__contains=sku)
    if id_marca != '0':
        query = query.where(marca_id=id_marca)
        query2 = Query().from_table(Marca, ['NOMBRE']).where(id=id_marca)
        nombre_marca = query2.select()

    productos = query.select()
    
    if len(nombre_marca) > 0:
        for producto in productos:
            producto['NOMBRE_MARCA'] = nombre_marca[0]['NOMBRE']

    return render(request, 'tienda/admin/productos/productos.html',
                  {
                    'productos': productos,
                    'marcas': obtener_marcas()
                  })

@login_required(login_url='login_admin')
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

@login_required(login_url='login_admin')
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

@login_required(login_url='login_admin')
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

@login_required(login_url='login_admin')
def cancelar_producto(request):
    """Redirige a la página principal del módulo Productos.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('productos_admin'))


# ----- Clientes ------
def ver_clientes_admin(request):
    """Muestra la página de gestión de Clientes.

    Args:

    Returns:
        Una página
    """

    run = Cliente.objects.all()

    return render(request, 'tienda/admin/usuarios/clientes.html',
                  {
                    'run': run
                  })


def agregar_clientes_admin(request):
    """Agrega un cliente a la base de datos

    Args:

    Returns:
        Una página
    """

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
    """Retorna una lista de clientes dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
    """

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
    """Actualiza un cliente segun su id
    Args:
        id (int): id del cliente a modificar
    Returns:
        Una página
    """

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


def eliminar_cliente_admin(request, id):
    """Actualiza un cliente segun su id

    Args:
        id (int): id del cliente a eliminar
    Returns:
        Una página
    """

    cliente = Cliente.objects.get(usuario_id=id)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('clientes_admin')

    return render(request, 'tienda/admin/usuarios/eliminar_cliente.html',
                  {
                      'cliente': cliente
                  })


def cancelar_cliente_admin(request):
    """Redirige a la página principal del módulo Clientes.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('clientes_admin'))


# ----- Administrador ------
def ver_administrador_admin(request):
    """Muestra la página de gestión de Administradores.

    Args:

    Returns:
        Una página
    """

    run = Administrador.objects.all()

    return render(request, 'tienda/admin/usuarios/administrador.html',
                  {
                    'run': run
                  })


def agregar_administrador_admin(request):
    """Agrega un administrador a la base de datos

    Args:

    Returns:
        Una página
    """

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
    """Retorna una lista de administradores dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
    """

    run = request.GET.get('run')
    appaterno= request.GET.get('appaterno')
    genero = request.GET.get('genero')
    administradores = Administrador.objects.all()

    # Busca tres campos
    if run != '' and appaterno != '' and genero != '':
        administradores = Administrador.objects.filter(run__icontains=run, appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo dos campos
    elif run != '' and appaterno != '':
        administradores = Administrador.objects.filter(run__icontains=run, appaterno__icontains=appaterno)
    elif run != '' and genero != '':
        administradores = Administrador.objects.filter(run__icontains=run, genero__icontains=genero)
    elif appaterno != '' and genero != '':
        administradores = Administrador.objects.filter(appaterno__icontains=appaterno, genero__icontains=genero)
    # Busca solo un campo
    elif run != '':
        administradores = Administrador.objects.filter(run__icontains=run)
    elif appaterno != '':
        administradores = Administrador.objects.filter(appaterno__icontains=appaterno)
    elif genero != '':
        administradores = Administrador.objects.filter(genero__icontains=genero)


    return render(request, 'tienda/admin/usuarios/administrador.html',
                {
                'administradores': administradores
                })


def cancelar_administrador_admin(request):
    """Redirige a la página principal del módulo Administradores.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('administrador_admin'))



def actualizar_administrador_admin(request, id):
    """Actualiza un administrador segun su id

    Args:
        id (int): id del administrador a modificar

    Returns:
        Una página
    """

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
    """Actualiza un administrador segun su id

    Args:
        id (int): id del administrador a eliminar

    Returns:
        Una página
    """
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
    """Muestra la página de gestión de Empleados.

    Args:

    Returns:
        Una página
    """

    run = Empleado.objects.all()

    return render(request, 'tienda/admin/usuarios/empleado.html',
                  {
                    'run': run
                  })


def agregar_empleado_admin(request):
    """Agrega un empleado a la base de datos

    Args:

    Returns:
        Una página
    """

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
    """Retorna una lista de empleados dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
    """
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


def eliminar_empleado_admin(request, id):
    """Actualiza un empleado segun su id

    Args:
        id (int): id del empleado a eliminar
    Returns:
        Una página
    """

    empleado = Empleado.objects.get(usuario_id=id)

    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('empleado_admin')

    return render(request, 'tienda/admin/usuarios/eliminar_empleado.html',
                  {
                      'empleado': empleado
                  })


def actualizar_empleado_admin(request, id):
    """Actualiza un empleado segun su id

    Args:
        id (int): id del empleado a modificar

    Returns:
        Una página
    """

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

def cancelar_empleado_admin(request):
    """Redirige a la página principal del módulo Empleados.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('empleado_admin'))

# ----- Vendedor ------
def ver_vendedor_admin(request):
    """Muestra la página de gestión de Vendedores.

    Args:

    Returns:
        Una página
    """

    run = Vendedor.objects.all()

    return render(request, 'tienda/admin/usuarios/vendedor.html',
                  {
                    'run': run
                  })


def agregar_vendedor_admin(request):
    """Agrega un vendedor a la base de datos

    Args:

    Returns:
        Una página
    """

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
    """Retorna una lista de vendedores dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
    """

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
    """Actualiza un vendedor segun su id

    Args:
        id (int): id del vendedor a modificar

    Returns:
        Una página
    """

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


def eliminar_vendedor_admin(request, id):
    """Actualiza un vendedor segun su id

    Args:
        id (int): id del vendedor a eliminar
    Returns:
        Una página
    """

    vendedor = Vendedor.objects.get(usuario_id=id)

    if request.method == 'POST':
        vendedor.delete()
        messages.success(request, 'Vendedor eliminado exitosamente.')
        return redirect('vendedor_admin')

    return render(request, 'tienda/admin/usuarios/eliminar_vendedor.html',
                  {
                      'vendedor': vendedor
                  })

def cancelar_vendedor_admin(request):
    """Redirige a la página principal del módulo Vendedores.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('vendedor_admin'))
# ---------------------- Boletas y Facturas ---------------------------- #
@login_required(login_url='login_admin')
def administrar_boletas(request):
    """Muestra la página de gestión de boletas.

    Args:
        clase_administrada: nombre de la clase para ser utilizado en el código de la plantilla
        nombre_clase: nombre de la clase que se muestra al usuario
        coleccion: colleción de objetos para iterar
        url_busqueda: url que se usará para filtrar la colección
        url_agregar: url que se usará para agregar un objeto a la colección
    Returns:
        Una página
    """
    boletas = Boleta.objects.all().prefetch_related('compra')
    clientes = Cliente.objects.all()
    estados = ['Anulada', 'Vigente']
    return render(request, 'tienda/admin/byf/boleta_factura.html',
                {
                    'clase_administrada': 'boleta',
                    'nombre_clase': 'Boletas',
                    'coleccion': boletas,
                    'clientes': clientes,
                    'estados': estados,
                    'url_busqueda': 'buscar_ordenes',
                    'url_agregar': 'agregar_orden'
                })

# ------------------ Ordenes de Compra ------------------
@login_required(login_url='login_admin')
def cancelar_orden(request):
    """Redirige a la página principal del módulo Ordenes de Compra.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('oc_admin'))

@login_required(login_url='login_admin')
def administrar_oc(request):
    """Muestra la página de gestión de ordenes de compra.

    Args:
        clase_administrada: nombre de la clase para ser utilizado en el código de la plantilla
        nombre_clase: nombre de la clase que se muestra al usuario
        coleccion: colleción de objetos para iterar
        url_busqueda: url que se usará para filtrar la colección
        url_agregar: url que se usará para agregar un objeto a la colección
    Returns:
        Una página
    """
    ordenes = OrdenDeCompra.objects.all().prefetch_related('proveedor')
    proveedores = Proveedor.objects.all()
    estados = OrdenDeCompra.estado_choices
    return render(request, 'tienda/admin/ordenes_compra/ordenes_compra.html',
                {
                    'clase_administrada': 'orden_de_compra',
                    'nombre_clase': 'Orden de compra',
                    'coleccion': ordenes,
                    'proveedores': proveedores,
                    'estados': estados,
                    'url_busqueda': 'buscar_ordenes',
                    'url_agregar': 'agregar_orden'
                })

@login_required(login_url='login_admin')
def actualizar_orden(request, id):
    """Actualiza una orden segun su id

    Args:
        id (int): id de la orden a modificar
    Returns:
        Una página
    """
    edita_orden = True

    orden = OrdenDeCompra.objects.get(id=id)
    ItemFormSet = modelformset_factory(ProductoOc, fields=('producto', 'orden_de_compra', 'cantidad'))

    if request.method == "POST":
        form = OrdenForm(request.POST, instance=orden)
        formset = ItemFormSet(request.POST, prefix='item')

        if form.is_valid():
            for item in formset:
                if item.is_valid():
                    id_item = int(0 if item['id'].value() == '' else item['id'].value())
                    cantidad = int(item['cantidad'].value())
                    if cantidad > 0:
                        item.save()
                    else:
                        ProductoOc.objects.get(id=id_item).delete()
            form.save()
            messages.success(request, 'Orden actualizada exitosamente.')
            return redirect('oc_admin')
        else:
            messages.error(request, 'No se ha podido actualizar la orden')
            return redirect('oc_admin')

    else:
        form = OrdenForm(instance=orden)
        itemForms = ItemFormSet(queryset=ProductoOc.objects.filter(orden_de_compra__id=id), prefix='item',initial=[{
                    'orden_de_compra': id,
                }])

        return render(request, 'tienda/admin/ordenes_compra/orden_form.html',
                      {
                          'id': id,
                          'form': form,
                          'edita': edita_orden,
                          'items': itemForms
                      })

@login_required(login_url='login_admin')
def eliminar_orden(request, id):
    """Elimina una orden de compra segun su id

    Args:
        id (int): id de la orden a eliminar
    Returns:
        Una página
    """

    orden = OrdenDeCompra.objects.get(id=id)

    if request.method == 'POST':
        orden.delete()
        messages.success(request, 'Orden de compra eliminada exitosamente.')
        return redirect('oc_admin')

    return render(request, 'tienda/admin/ordenes_compra/eliminar_orden.html',
                  {
                      'orden': orden
                  })

@login_required(login_url='login_admin')
def agregar_orden(request):
    """Agrega una orden de compra a la base de datos

    Args:

    Returns:
        Una página
    """

    if request.method == 'POST':

        form = OrdenForm(request.POST)

        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.save()
            messages.success(request, 'Orden de compra agregada exitosamente.')

            return redirect('oc_admin')
    else:
        form = OrdenForm({
            'fecha_recepcion': generar_fecha(7)
            })
        return render(request, 'tienda/admin/ordenes_compra/orden_form.html',
                      {
                        'form': form
                      })

@login_required(login_url='login_admin')
def buscar_ordenes(request):
    """Retorna una lista de ordenes de compra dependiendo de los filtros
    ingresados

    Args:

    Returns:
        Una página
        productos: Queryset con los productos
    """
    params = request.GET

    proveedores = Proveedor.objects.all()
    estados = OrdenDeCompra.estado_choices

    ordenes = utils.filtrar_equals(params, OrdenDeCompra)

    return render(request, 'tienda/admin/ordenes_compra/ordenes_compra.html',
                {
                    'clase_administrada': 'orden_de_compra',
                    'nombre_clase': 'Orden de compra',
                    'coleccion': ordenes,
                    'proveedores': proveedores,
                    'estados': estados,
                    'url_busqueda': 'buscar_ordenes',
                    'url_agregar': 'agregar_orden'
                })

@login_required(login_url='login_admin')
def recibir_orden(request, id):
    orden = OrdenDeCompra.objects.get(id=id)

    if orden.estado == 'PENDIENTE':
        items = ProductoOc.objects.filter(orden_de_compra__id=id).prefetch_related('producto')
        for item in items:
            item.producto.stock += item.cantidad
            item.producto.save()
        orden.estado = 'RECIBIDA'
        orden.save()
        messages.success(request, 'Orden de compra recibida exitosamente.')
        return redirect(reverse('oc_admin'))
    else:
        messages.error(request, 'Solo se pueden recibir ordenes pendientes')
        return redirect(reverse('oc_admin'))

def eliminar_item(request, id, idOrden):
    item = ProductoOc.objects.get(id=id)
    orden = OrdenDeCompra.objects.get(id=idOrden)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item de compra eliminado exitosamente.')
        return redirect(reverse('actualizar_orden', kwargs={'id':idOrden}))
    else:
        return render(request, 'tienda/admin/ordenes_compra/eliminar_item.html',
              {
                  'item': item,
                  'orden': orden
              })

@login_required(login_url='login_admin')
def agregar_item(request, idOrden):
    oc = OrdenDeCompra.objects.get(id=idOrden)

    orden = ProductoOc.objects.create(
        orden_de_compra = oc,
        cantidad = 0,
        producto = Producto.objects.first()
    )

    logging.warning(orden)
    return redirect(reverse('actualizar_orden', kwargs={'id':idOrden}))

@login_required(login_url='login_admin')
def cancelar_item(request, id):
    return redirect(reverse('actualizar_orden', kwargs={'id':id}))
# ------------------ Proveedores ------------------

@login_required(login_url='login_admin')
def cancelar_proveedor(request):
    """Redirige a la página principal del módulo proveedores.

    Args:

    Returns:
        Una página
    """

    return redirect(reverse('administrar_proveedores'))

@login_required(login_url='login_admin')
def administrar_proveedores(request):
    """Muestra la página de gestión de proveedores.

    Args:
        clase_administrada: nombre de la clase para ser utilizado en el código de la plantilla
        nombre_clase: nombre de la clase que se muestra al usuario
        coleccion: colleción de objetos para iterar
        url_busqueda: url que se usará para filtrar la colección
        url_agregar: url que se usará para agregar un objeto a la colección
    Returns:
        Una página
    """
    proveedores = Proveedor.objects.all()

    return render(request, 'tienda/admin/proveedores/proveedores.html',
                {
                    'clase_administrada': 'proveedor',
                    'nombre_clase': 'proveedor',
                    'coleccion': proveedores,
                    'url_busqueda': 'buscar_proveedores',
                    'url_agregar': 'agregar_proveedor'
                })

@login_required(login_url='login_admin')
def buscar_proveedores(request):

    params = request.GET
    proveedores = utils.filtrar_icontains(params, Proveedor)

    return render(request, 'tienda/admin/proveedores/proveedores.html',
                {
                    'clase_administrada': 'proveedor',
                    'nombre_clase': 'proveedor',
                    'coleccion': proveedores,
                    'url_busqueda': 'buscar_proveedores',
                    'url_agregar': 'agregar_proveedor'
                })

@login_required(login_url='login_admin')
def actualizar_proveedor(request, id):
    """Actualiza una proveedor segun su id

    Args:
        id (int): id de la proveedor a modificar
    Returns:
        Una página
    """
    edita_proveedor = True

    proveedor = Proveedor.objects.get(id=id)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'proveedor actualizado exitosamente.')
            return redirect('administrar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
        return render(request, 'tienda/admin/proveedores/proveedor_form.html',
                      {
                          'form': form,
                          'edita': edita_proveedor,
                      })

@login_required(login_url='login_admin')
def eliminar_proveedor(request, id):
    """Elimina una proveedor segun su id

    Args:
        id (int): id de la proveedor a eliminar
    Returns:
        Una página
    """

    proveedor = Proveedor.objects.get(id=id)

    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'proveedor eliminada exitosamente.')
        return redirect('administrar_proveedores')

    return render(request, 'tienda/admin/proveedores/eliminar_proveedor.html',
                  {
                      'proveedor': proveedor
                  })

@login_required(login_url='login_admin')
def agregar_proveedor(request):
    """Agrega una proveedor a la base de datos

    Args:

    Returns:
        Una página
    """

    if request.method == 'POST':

        form = ProveedorForm(request.POST)

        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.save()
            messages.success(request, 'proveedor agregada exitosamente.')

            return redirect('administrar_proveedores')
    else:
        form = ProveedorForm()
        return render(request, 'tienda/admin/proveedores/proveedor_form.html',
                      {
                        'form': form
                      })

# --------------------------------------------------------------------------------------------
#   Prueba Autenticacion
#---------------------------------------------------------------------------------------------
def login_cliente(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                cliente = Cliente.objects.filter(user=user).first()
                if cliente is None and user.groups.all()[0].name == 'administrador':
                    return redirect('login_admin')
            if user is not None and cliente is not None:

                login(request, user)
                messages.success(request, f"Inicio de sesión exitoso. Bienvenido/a {cliente.nombres} {cliente.appaterno}")
                # Cada vez que un usuario logee, se creara una instancia de carrito.
                carro = Carro.objects.filter(cliente=request.user.id).first()

                if carro is None:
                    fecha = datetime.now()
                    carro_id = fecha.strftime("%d%m%y%H%M%S") + str(request.user.id);
                    Carro.objects.create(carro_id=carro_id, cliente=request.user)

                return redirect('home')
            else:
                messages.error(request, 'El nombre de usuario o la contraseña son incorrectos.')
                return redirect(reverse('login_cliente'))

        else:
            return render(request, 'tienda/auth/login.html', {})


def logout_cliente(request):
    # De momento, el carro se elimina al cerrar sesion
    # carrito = Carro.objects.get(cliente=request.user)
    # carrito.delete()
    logout(request)
    messages.info(request, "Cierre de sesión exitoso.")
    return redirect('home')

@unauthenticated_user
def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Inicio de sesión exitoso.")
            return redirect('admin')
        else:
            messages.error(request, 'El nombre de usuario o la contraseña son incorrectos.')
            return redirect(reverse('login_admin'))

    else:
        return render(request, 'tienda/admin/auth/login_admin.html', {})

def logout_admin(request):
    logout(request)
    messages.info(request, "Cierre de sesión exitoso.")
    return redirect('login_admin')

def registro(request):
    
    if request.user.is_authenticated:
        return redirect('home')    
    else:
        if request.method == 'POST':
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                user = form.save()
                nombre = form.cleaned_data.get('nombres')

                messages.success(request, f"{nombre}, la creación de tu cuenta ha sido exitosa." +
                    " Ahora ya puedes iniciar sesión con tu nombre de usuario.")
                return redirect('login_cliente')
            else:
                messages.error(request, "Error al crear una nueva cuenta.")
                return redirect(reverse('registro_cliente'))
        else:
            form = CrearUsuarioForm()
            return render(request, 'tienda/auth/registro_cliente.html',
                            {
                                'form': form
                            })

@login_required(login_url='login_admin')
@autorizar_usuarios(roles_permitidos=['administrador'])
def registro_admin(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente.")
            return redirect(reverse('registro_admin'))
        else:
            messages.error(request, "Error al crear nuevo usuario.")
            return redirect(reverse('registro_admin'))
    else:
        form = CrearUsuarioForm()
        return render(request, 'tienda/admin/auth/registro_admin.html',
                        {
                            'form': form
                        })

# ----------------------- REPORTE ------------------------------------------------
def ver_reporte(request):
    logeos_cliente = 0
    usuarios = []
    weekdays = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    log_weekdays = []
    log_stats = {}
    comienzo = generar_fecha(-120, "%Y-%m-%d")
    fin = generar_fecha(0, "%Y-%m-%d")

    logeos = Actividad.objects.filter(fecha_hora__gte=comienzo, fecha_hora__lte=fin)

    for logeo in logeos:
        if logeo.usuario is not None:
            user = User.objects.get(id=logeo.usuario.id)
            usuarios.append(user)
        log_weekdays.append(logeo.fecha_hora.weekday())
    for usuario in usuarios:
        if usuario.groups.all()[0].name == 'cliente':
            logeos_cliente += 1
    for day in weekdays:
        log_stats[day] = log_weekdays.count(weekdays.index(day))
    dias = list(log_stats.keys())
    valores = list(log_stats.values())
    return render(request, 'tienda/admin/reporte/reporte.html', 
        {
            'logeos': logeos_cliente,
            'stats': log_stats,
            'dias': dias,
            'valores': valores,
            'comienzo': comienzo,
            'fin': fin
        })

