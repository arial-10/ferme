# Generated by Django 3.0.6 on 2020-05-30 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=50)),
                ('cod_admin', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Administrador',
            },
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('carro_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Carro',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('genero', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(default=0)),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Cliente')),
            ],
            options={
                'db_table': 'Compra',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=50)),
                ('cod_empleado', models.CharField(max_length=6)),
                ('sucursal', models.CharField(max_length=55)),
                ('fecha_contrato', models.DateField()),
                ('area', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'OrdenDeCompra',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('stock_critico', models.IntegerField()),
                ('disponibilidad', models.CharField(max_length=1)),
                ('precio_normal', models.IntegerField()),
                ('precio_oferta', models.IntegerField()),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.Marca')),
            ],
            options={
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=55)),
                ('sector_comercial', models.CharField(max_length=55)),
                ('direccion', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=55)),
                ('fono', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=50)),
                ('cod_vendedor', models.CharField(max_length=6)),
                ('sucursal', models.CharField(max_length=55)),
                ('fecha_contrato', models.DateField()),
            ],
            options={
                'db_table': 'Vendedor',
            },
        ),
        migrations.CreateModel(
            name='RetiroTienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateField()),
                ('rut_receptor', models.CharField(max_length=12)),
                ('estado', models.CharField(max_length=20)),
                ('sucursal', models.CharField(max_length=20)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Compra')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Empleado')),
            ],
            options={
                'db_table': 'RetiroTienda',
            },
        ),
        migrations.CreateModel(
            name='ProductoOc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.OrdenDeCompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
            ],
            options={
                'db_table': 'ProductoOc',
            },
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Proveedor'),
        ),
        migrations.CreateModel(
            name='NotaCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=45)),
                ('fecha_compra', models.DateField()),
                ('terminal', models.IntegerField()),
                ('tipo_pago', models.IntegerField()),
                ('anulada', models.CharField(max_length=1)),
                ('fecha_anulacion', models.DateField()),
                ('doc_asociado', models.CharField(max_length=10)),
                ('desc_motivo', models.CharField(max_length=255)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Compra')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Empleado')),
            ],
            options={
                'db_table': 'NotaCredito',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=45)),
                ('fecha_compra', models.DateField()),
                ('terminal', models.IntegerField()),
                ('tipo_pago', models.IntegerField()),
                ('anulada', models.CharField(max_length=1)),
                ('rut_empresa', models.CharField(max_length=12)),
                ('iva', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Compra')),
            ],
            options={
                'db_table': 'Factura',
            },
        ),
        migrations.CreateModel(
            name='DespachoDomicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateField()),
                ('rut_receptor', models.CharField(max_length=12)),
                ('estado', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono_contacto', models.CharField(max_length=12)),
                ('comuna', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Compra')),
            ],
            options={
                'db_table': 'DespachoDomicilio',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Vendedor'),
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Categoria')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
            ],
            options={
                'db_table': 'CategoriaProducto',
            },
        ),
        migrations.CreateModel(
            name='CarroProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Carro')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.Producto')),
            ],
            options={
                'db_table': 'CarroProducto',
            },
        ),
        migrations.AddField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Cliente'),
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=45)),
                ('fecha_compra', models.DateField()),
                ('terminal', models.IntegerField()),
                ('tipo_pago', models.IntegerField()),
                ('anulada', models.CharField(max_length=1)),
                ('rut_persona', models.CharField(max_length=12)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Compra')),
            ],
            options={
                'db_table': 'Boleta',
            },
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Actividad',
            },
        ),
    ]
