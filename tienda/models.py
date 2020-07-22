from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .validators import *
from .utils import *
from datetime import datetime, timedelta, tzinfo, timezone
import pytz


class Administrador(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.CharField(default='+569 ', max_length=12)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=150)
    cod_admin = models.CharField(max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Administrador'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Empleado(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.CharField(default='+569 ', max_length=12)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    cod_empleado = models.CharField(max_length=6)
    sucursal = models.CharField(max_length=55)
    fecha_contrato = models.DateField()
    area = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Empleado'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Cliente(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.CharField(default='+569 ', max_length=12)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno

class Vendedor(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.CharField(default='+569 ', max_length=12)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    cod_vendedor = models.CharField(max_length=6)
    sucursal = models.CharField(max_length=55)
    fecha_contrato = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Vendedor'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    monto_total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Compra'


class Actividad(models.Model):
    fecha_hora = models.DateTimeField()
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
                                null=True)

    class Meta:
        db_table = 'Actividad'


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Categoria'

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Marca'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    producto_id = models.CharField(max_length=17, primary_key=True)
    sku = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    disponibilidad = models.CharField(max_length=1)
    precio_normal = models.IntegerField()
    precio_oferta = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    url_img = models.CharField(max_length=200)

    class Meta:
        db_table = 'Producto'

    def __str__(self):
        return self.nombre


class CategoriaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CategoriaProducto'

    def __str__(self):
        return self.producto.nombre


class Carro(models.Model):
    carro_id = models.CharField(max_length=15, primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Carro'

    def __str__(self):
        return self.carro_id


class CarroProducto(models.Model):
    cantidad = models.IntegerField()
    precio = models.CharField(max_length=10)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,
                                 null=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CarroProducto'

    def __str__(self):
        return self.producto.nombre


class Proveedor(models.Model):
    #esto necesita un RUN
    razon_social = models.CharField(max_length=55)
    sector_comercial = models.CharField(max_length=55)
    direccion = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    fono = models.CharField(max_length=55)

    class Meta:
        db_table = 'Proveedor'

    def __str__(self):
        return self.razon_social


class OrdenDeCompra(models.Model):
    estado_choices = (
        ('RECIBIDA', 'RECIBIDA'),
        ('PENDIENTE', 'PENDIENTE'),
        ('ANULADA', 'ANULADA'),
        ('ENVIADA', 'ENVIADA')
    )

    fecha_recepcion = models.DateField()
    estado = models.CharField(max_length=20, choices=estado_choices)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'OrdenDeCompra'


class ProductoOc(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    orden_de_compra = models.ForeignKey(OrdenDeCompra,
                                        on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'ProductoOc'


class RetiroTienda(models.Model):
    fecha_entrega = models.DateField()
    rut_receptor = models.CharField(max_length=12)
    estado = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=20)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RetiroTienda'


class DespachoDomicilio(models.Model):
    fecha_entrega = models.DateField()
    rut_receptor = models.CharField(max_length=12)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    telefono_contacto = models.CharField(max_length=12)
    comuna = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20, blank = True, null = True,)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    class Meta:
        db_table = 'DespachoDomicilio'


class Boleta(models.Model):
    documento_id = models.CharField(max_length=38)
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=45)
    fecha_compra = models.DateField()
    terminal = models.IntegerField()
    tipo_pago = models.CharField(max_length=11)
    anulada = models.CharField(max_length=20)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    rut_persona = models.CharField(max_length=12)
    
    @property
    def sid(self):
        return "B%05d" % self.id

    class Meta:
        db_table = 'Boleta'


class Factura(models.Model):
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=45)
    fecha_compra = models.DateField()
    terminal = models.IntegerField()
    tipo_pago = models.CharField(max_length=11)
    estado = models.CharField(max_length=20)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    rut_empresa = models.CharField(max_length=12)
    iva = models.IntegerField()

    class Meta:
        db_table = 'Factura'


class NotaCredito(models.Model):
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=45)
    fecha_compra = models.DateField()
    terminal = models.IntegerField()
    tipo_pago = models.CharField(max_length=11)
    estado = models.CharField(max_length=20)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_anulacion = models.DateField()
    doc_asociado = models.CharField(max_length=10)
    desc_motivo = models.CharField(max_length=255)

    class Meta:
        db_table = 'NotaCredito'

class ProductoCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'ProductoCompra'


class ProveedorProducto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,
                                 null=True)

    class Meta:
        db_table = 'ProveedorProducto'

# ----------------------------------------------------------------------------#
#               AUNTENTICACION DISTINTOS USUARIOS                             #
# ----------------------------------------------------------------------------#

@receiver(pre_save, sender=Cliente)
def crear_usuario_cliente(sender, instance, **kwargs):
    print('Creando grupo usuario para el cliente...')
    user = User.objects.create_user(
            instance.nombre_usuario,
            instance.email,
            instance.contrasena
        )
    instance.user = user
    print('Agregando al grupo...')
    grupo, created = Group.objects.get_or_create(name='cliente')
    user.groups.add(grupo)

@receiver(pre_save, sender=Empleado)
def crear_usuario_empleado(sender, instance, **kwargs):
    user = User.objects.create_user(
            instance.nombre_usuario,
            instance.email,
            instance.contrasena
        )
    instance.user = user
    grupo, created = Group.objects.get_or_create(name='empleado')
    user.groups.add(grupo)

@receiver(pre_save, sender=Administrador)
def crear_usuario_administrador(sender, instance, **kwargs):
    if instance.user is None:
        user = User.objects.create_user(
                instance.nombre_usuario,
                instance.email,
                instance.contrasena
            )
        instance.user = user
    print('Creando grupo de administradores')
    grupo, created = Group.objects.get_or_create(name='administrador')
    instance.user.groups.add(grupo)

    
@receiver(pre_save, sender=Vendedor)
def crear_usuario_vendedor(sender, instance, **kwargs):
    user = User.objects.create_user(
            instance.nombre_usuario,
            instance.email,
            instance.contrasena
        )
    instance.user = user
    grupo, created = Group.objects.get_or_create(name='vendedor')
    user.groups.add(grupo)

@receiver(post_save, sender=User)
def crear_grupo_superusuario(sender, instance, **kwargs):
    if instance.is_superuser:
        grupo, created = Group.objects.get_or_create(name='administrador')
        instance.groups.add(grupo)
        admin = Administrador.objects.filter(nombre_usuario=instance.username).first()
        if admin is None:
            admin = Administrador.objects.create(
                user=instance, 
                fecha_nacimiento=generar_fecha(0, '%Y-%m-%d'),
                run = 9999999,
                nombres = instance.username,
                nombre_usuario = instance.username,
                contrasena = instance.password
            )
            print("Se ha creado un usuario administrador para este usuario de django, con campos provisorios, por favor revise su panel de administracion")

@receiver(user_logged_in)
def login_logger(request, user, **kwargs):
    Actividad.objects.create(
            fecha_hora = datetime.now(),
            usuario = user
        )

@receiver(post_save, sender=Boleta)
def generar_id_boleta(sender, instance, **kwargs):
    instance.documento_id = 'B' + str(instance.id)
