from django.db import models
from django.utils import timezone

class Administrador(models.Model):
	run = models.CharField(max_length=12, default='NA')
	nombres = models.CharField(max_length=50, default='NA')
	appaterno = models.CharField(max_length=50, default='NA')
	apmaterno = models.CharField(max_length=50, default='NA')
	fecha_nacimiento = models.DateField(default=0)
	genero = models.CharField(max_length=6, default='NA')
	email = models.CharField(max_length=50, default='NA')
	telefono = models.IntegerField(default=0)
	nombre_usuario = models.CharField(max_length=40, default='NA')
	contrasena = models.CharField(max_length=50, default='NA')
	cod_admin = models.CharField(max_length=6, default='NA')

	def __str__(self):
		return self.nombre


class Empleado(models.Model):
	run = models.CharField(max_length=12, default='NA')
	nombres = models.CharField(max_length=50, default='NA')
	appaterno = models.CharField(max_length=50, default='NA')
	apmaterno = models.CharField(max_length=50, default='NA')
	fecha_nacimiento = models.DateField(default=0)
	genero = models.CharField(max_length=6, default='NA')
	email = models.CharField(max_length=50, default='NA')
	telefono = models.IntegerField(default=0)
	nombre_usuario = models.CharField(max_length=40, default='NA')
	contrasena = models.CharField(max_length=50, default='NA')
	cod_empleado = models.CharField(max_length=6, default='NA')
	sucursal = models.CharField(max_length=55, default='NA')
	fecha_contrato = models.DateField(default=0)
	area = models.CharField(max_length=20, default='NA')

	def __str__(self):
		return self.nombre


class Cliente(models.Model):
	run = models.CharField(max_length=12, default='NA')
	nombres = models.CharField(max_length=50, default='NA')
	appaterno = models.CharField(max_length=50, default='NA')
	apmaterno = models.CharField(max_length=50, default='NA')
	fecha_nacimiento = models.DateField(default=0)
	genero = models.CharField(max_length=6, default='NA')
	email = models.CharField(max_length=50, default='NA')
	telefono = models.IntegerField(default=0)
	nombre_usuario = models.CharField(max_length=40, default='NA')
	contrasena = models.CharField(max_length=50, default='NA')
	direccion = models.CharField(max_length=50, default='NA')

	def __str__(self):
		return self.nombre


class Vendedor(models.Model):
	run = models.CharField(max_length=12, default='NA')
	nombres = models.CharField(max_length=50, default='NA')
	appaterno = models.CharField(max_length=50, default='NA')
	apmaterno = models.CharField(max_length=50, default='NA')
	fecha_nacimiento = models.DateField(default=0)
	genero = models.CharField(max_length=6, default='NA')
	email = models.CharField(max_length=50, default='NA')
	telefono = models.IntegerField(default=0)
	nombre_usuario = models.CharField(max_length=40, default='NA')
	contrasena = models.CharField(max_length=50, default='NA')
	cod_vendedor = models.CharField(max_length=6, default='NA')
	sucursal = models.CharField(max_length=55, default='NA')
	fecha_contrato = models.DateField(default=0)

	def __str__(self):
		return self.nombre


class Compra(models.Model):
	vendedor_cod_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, default=0)
	monto_total = models.IntegerField(default=0)
	cliente_usuario_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=0)

class Actividad(models.Model):
	fecha_hora = models.DateField(default=0)
	usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, default=0,
								null=True)


class Categoria(models.Model):
	nombre = models.CharField(max_length=50, default='NA')

	def __str__(self):
		return self.nombre


class Marca(models.Model):
	nombre = models.CharField(max_length=50, default='NA')

	def __str__(self):
		return self.nombre


class Producto(models.Model):
	sku = models.CharField(max_length=100, default='NA')
	nombre = models.CharField(max_length=100, default='NA')
	color = models.CharField(max_length=20, default='NA')
	descripcion = models.CharField(max_length=100, default='NA')
	stock = models.IntegerField(default=0)
	stock_critico = models.IntegerField(default=0)
	disponibilidad = models.CharField(max_length=1, default='NA')
	precio_normal = models.IntegerField(default=0)
	precio_oferta = models.IntegerField(default=0)
	marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, default=0)

	def __str__(self):
		return self.nombre


class CategoriaProducto(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=0)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)

	def __str__(self):
		return self.producto + ' - ' + self.categoria


class Carro(models.Model):
	carro_id = models.CharField(max_length=8, primary_key=True, default='NA')
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=0)

	def __str__(self):
		return self.carro_id


class CarroProducto(models.Model):
	cantidad = models.IntegerField(default=0)
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, default=0,
								 null=True)
	carro = models.ForeignKey(Carro, on_delete=models.CASCADE, default=0)

class Proveedor(models.Model):
	razon_social = models.CharField(max_length=55, default='NA')
	sector_comercial = models.CharField(max_length=55, default='NA')
	direccion = models.CharField(max_length=55, default='NA')
	email = models.CharField(max_length=55, default='NA')
	fono = models.CharField(max_length=55, default='NA')

class OrdenDeCompra(models.Model):
	fecha_recepcion = models.DateField(default=0)
	estado = models.CharField(max_length=20, default='NA')
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=0)

class ProductoOc(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=0)
	orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE, default=0)

class RetiroTienda(models.Model):
	fecha_entrega = models.DateField(default=0)
	rut_receptor = models.CharField(max_length=12, default='NA')
	estado = models.CharField(max_length=20, default='NA')
	sucursal = models.CharField(max_length=20, default='NA')
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, default=0)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)

class DespachoDomicilio(models.Model):
	fecha_entrega = models.DateField(default=0)
	rut_receptor = models.CharField(max_length=12, default='NA')
	estado = models.CharField(max_length=20, default='NA')
	direccion = models.CharField(max_length=60, default='NA')
	telefono_contacto = models.CharField(max_length=12, default='NA')
	comuna = models.CharField(max_length=20, default='NA')
	descripcion = models.CharField(max_length=20, default='NA')
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)

class Boleta(models.Model):
	sucursal = models.CharField(max_length=100, default='NA')
	direccion = models.CharField(max_length=100, default='NA')
	comuna = models.CharField(max_length=45, default='NA')
	fecha_compra = models.DateField(default=0)
	terminal = models.IntegerField(default=0)
	tipo_pago = models.IntegerField(default=0)
	anulada = models.CharField(max_length=1, default='NA')
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)
	rut_persona = models.CharField(max_length=12, default='NA')

class Factura(models.Model):
	sucursal = models.CharField(max_length=100, default='NA')
	direccion = models.CharField(max_length=100, default='NA')
	comuna = models.CharField(max_length=45, default='NA')
	fecha_compra = models.DateField(default=0)
	terminal = models.IntegerField(default=0)
	tipo_pago = models.IntegerField(default=0)
	anulada = models.CharField(max_length=1, default='NA')
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)
	rut_empresa = models.CharField(max_length=12, default='NA')
	iva = models.IntegerField(default=0)

class NotaCredito(models.Model):
	sucursal = models.CharField(max_length=100, default='NA')
	direccion = models.CharField(max_length=100, default='NA')
	comuna = models.CharField(max_length=45, default='NA')
	fecha_compra = models.DateField(default=0)
	terminal = models.IntegerField(default=0)
	tipo_pago = models.IntegerField(default=0)
	anulada = models.CharField(max_length=1, default='NA')
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, default=0)
	fecha_anulacion = models.DateField(default=0)
	doc_asociado = models.CharField(max_length=10, default='NA')
	desc_motivo = models.CharField(max_length=255, default='NA')
