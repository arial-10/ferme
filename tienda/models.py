from django.db import models
from django.utils import timezone

class Administrador(models.Model):
    usuario_id = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    cod_admin = models.CharField(max_length=6)

    class Meta:
        db_table = 'Administrador'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Empleado(models.Model):
    usuario_id = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    cod_empleado = models.CharField(max_length=6)
    sucursal = models.CharField(max_length=55)
    fecha_contrato = models.DateField()
    area = models.CharField(max_length=20)

    class Meta:
        db_table = 'Empleado'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Cliente(models.Model):
    usuario_id = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Vendedor(models.Model):
    usuario_id = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)
    cod_vendedor = models.CharField(max_length=6)
    sucursal = models.CharField(max_length=55)
    fecha_contrato = models.DateField()

    class Meta:
        db_table = 'Vendedor'

    def __str__(self):
        return self.nombres + ' ' + self.appaterno


class Compra(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_compra = models.IntegerField(primary_key=True)
    monto_total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Compra'


class Actividad(models.Model):
    fecha_hora = models.DateField()
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
                                null=True)

    class Meta:
        db_table = 'Actividad'


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Categoria'


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



class Carro(models.Model):
    carro_id = models.CharField(max_length=8, primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Carro'



class CarroProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,
                                 null=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CarroProducto'


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
        ('RECIBIDA', 'Recibida'),
        ('PENDIENTE', 'Pendiente'),
        ('ANULADA', 'Anulada'),
        ('ENVIADA', 'Enviada')
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
    descripcion = models.CharField(max_length=20)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    class Meta:
        db_table = 'DespachoDomicilio'


class Boleta(models.Model):
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=45)
    fecha_compra = models.DateField()
    terminal = models.IntegerField()
    tipo_pago = models.CharField(max_length=11)
    estado = models.CharField(max_length=20)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    rut_persona = models.CharField(max_length=12)

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
