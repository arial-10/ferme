from django.db import models


class Actividad(models.Model):
    fecha_hora = models.DateField()
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
                                null=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    sku = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    disponibilidad = models.CharField(max_length=1)
    precio_normal = models.IntegerField()
    precio_oferta = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


class CategoriaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto + ' - ' + self.categoria


class Carro(models.Model):
    carro_id = models.CharField(max_length=8, primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.carro_id


class CarroProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,
                                 null=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
