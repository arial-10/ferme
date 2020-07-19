from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        self.fields['sku'].required = False
        self.fields['nombre'].required = False
        self.fields['color'].required = False
        self.fields['descripcion'].required = False
        self.fields['disponibilidad'].required = False

    class Meta:
        model = Producto
        fields = ['producto_id', 'sku', 'nombre', 'color', 'descripcion',
                    'stock', 'stock_critico', 'disponibilidad',
                    'precio_normal', 'precio_oferta', 'marca']

        labels = {'producto_id': 'ID',
                    'sku': 'SKU',
                    'nombre': 'Nombre',
                    'color': 'Color',
                    'descripcion': 'Descripción',
                    'stock': 'Stock',
                    'stock_critico': 'Stock Crítico',
                    'disponibilidad': 'Disponibilidad',
                    'precio_normal': 'Precio Normal',
                    'precio_oferta': 'Precio Oferta',
                    'marca': 'Marca'}
        widgets = {
                    'producto_id': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 17
                    }),
                    'sku': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombre': forms.TextInput(attrs={
                        'class': 'form-control',
                    }),
                    'color': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'descripcion': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'stock': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'stock_critico': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'disponibilidad': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 1
                    }),
                    'precio_normal': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'precio_oferta': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'marca': forms.Select(attrs={
                        'class': 'form-control'
                    }),
        }


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['usuario_id', 'run', 'nombres', 'appaterno', 'apmaterno', 'fecha_nacimiento',
                    'genero', 'email', 'telefono',
                    'nombre_usuario', 'contrasena', 'direccion']
        required = [
                    'usuario_id',
                    'run',
                    'nombres',
                    'appaterno',
                    'apmaterno',
                    'fecha_nacimiento',
                    'genero',
                    'email',
                    'telefono',
                    'nombre_usuario',
                    'contrasena',
                    'direccion'
        ]
        labels = {  'usuario_id': 'usuario_id',
                    'run': 'run',
                    'nombres': 'Nombres',
                    'appaterno': 'Apellido paterno',
                    'apmaterno': 'Apellido materno',
                    'fecha_nacimiento': 'Fecha nacimiento',
                    'genero': 'Genero',
                    'email': 'Email',
                    'telefono': 'Telefono',
                    'nombre_usuario': 'Nombre usuario',
                    'contrasena': 'Contrasena',
                    'direccion': 'Direccion'
                    }
        widgets = {
                    'usuario_id': forms.NumberInput(attrs={
                    'class': 'form-control'
                    }),
                    'run': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombres': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'appaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'apmaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'fecha_nacimiento': forms.DateInput(attrs={
                        'class': 'form-control'
                    }),
                    'genero': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 6
                    }),
                    'email': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'telefono': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'nombre_usuario': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'contrasena': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'direccion': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
    }


class AdministradorForm(ModelForm):

    class Meta:
        model = Administrador
        fields = ['usuario_id', 'run', 'nombres', 'appaterno', 'apmaterno', 'fecha_nacimiento',
                    'genero', 'email', 'telefono',
                    'nombre_usuario', 'contrasena', 'cod_admin']
        required = [
                    'usuario_id',
                    'run',
                    'nombres',
                    'appaterno',
                    'apmaterno',
                    'fecha_nacimiento',
                    'genero',
                    'email',
                    'telefono',
                    'nombre_usuario',
                    'contrasena',
                    'cod_admin'
        ]
        labels = {  'usuario_id': 'usuario_id',
                    'run': 'run',
                    'nombres': 'Nombres',
                    'appaterno': 'Apellido paterno',
                    'apmaterno': 'Apellido materno',
                    'fecha_nacimiento': 'Fecha nacimiento',
                    'genero': 'Genero',
                    'email': 'Email',
                    'telefono': 'Telefono',
                    'nombre_usuario': 'Nombre usuario',
                    'contrasena': 'Contrasena',
                    'cod_admin': 'Codigo admin'
                    }
        widgets = {
                    'usuario_id': forms.NumberInput(attrs={
                    'class': 'form-control'
                    }),
                    'run': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombres': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'appaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'apmaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'fecha_nacimiento': forms.DateInput(attrs={
                        'class': 'form-control'
                    }),
                    'genero': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 6
                    }),
                    'email': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'telefono': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'nombre_usuario': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'contrasena': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'cod_admin': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),

    }


class EmpleadoForm(ModelForm):

    class Meta:
        model = Empleado
        fields = ['usuario_id', 'run', 'nombres', 'appaterno', 'apmaterno', 'fecha_nacimiento',
                    'genero', 'email', 'telefono',
                    'nombre_usuario', 'contrasena', 'cod_empleado', 'sucursal', 'fecha_contrato', 'area']
        required = [
                    'usuario_id',
                    'run',
                    'nombres',
                    'appaterno',
                    'apmaterno',
                    'fecha_nacimiento',
                    'genero',
                    'email',
                    'telefono',
                    'nombre_usuario',
                    'contrasena',
                    'cod_empleado',
                    'sucursal',
                    'fecha_contrato',
                    'area'
        ]
        labels = {  'usuario_id': 'usuario_id',
                    'run': 'run',
                    'nombres': 'Nombres',
                    'appaterno': 'Apellido paterno',
                    'apmaterno': 'Apellido materno',
                    'fecha_nacimiento': 'Fecha nacimiento',
                    'genero': 'Genero',
                    'email': 'Email',
                    'telefono': 'Telefono',
                    'nombre_usuario': 'Nombre usuario',
                    'contrasena': 'Contrasena',
                    'cod_empleado': 'Codigo empleado',
                    'sucursal': 'Sucursal',
                    'fecha_contrato': 'Fecha contrato',
                    'area': 'Area'
                    }
        widgets = {
                    'usuario_id': forms.NumberInput(attrs={
                    'class': 'form-control'
                    }),
                    'run': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombres': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'appaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'apmaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'fecha_nacimiento': forms.DateInput(attrs={
                        'class': 'form-control'
                    }),
                    'genero': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 6
                    }),
                    'email': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'telefono': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'nombre_usuario': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'contrasena': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'cod_empleado': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'sucursal': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'fecha_contrato': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'area': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),


    }


class VendedorForm(ModelForm):

    class Meta:
        model = Vendedor
        fields = ['usuario_id', 'run', 'nombres', 'appaterno', 'apmaterno', 'fecha_nacimiento',
                    'genero', 'email', 'telefono',
                    'nombre_usuario', 'contrasena', 'cod_vendedor', 'sucursal', 'fecha_contrato']
        required = [
                    'usuario_id',
                    'run',
                    'nombres',
                    'appaterno',
                    'apmaterno',
                    'fecha_nacimiento',
                    'genero',
                    'email',
                    'telefono',
                    'nombre_usuario',
                    'contrasena',
                    'cod_vendedor',
                    'sucursal',
                    'fecha_contrato'

        ]
        labels = {  'usuario_id': 'usuario_id',
                    'run': 'run',
                    'nombres': 'Nombres',
                    'appaterno': 'Apellido paterno',
                    'apmaterno': 'Apellido materno',
                    'fecha_nacimiento': 'Fecha nacimiento',
                    'genero': 'Genero',
                    'email': 'Email',
                    'telefono': 'Telefono',
                    'nombre_usuario': 'Nombre usuario',
                    'contrasena': 'Contrasena',
                    'cod_vendedor': 'Codigo empleado',
                    'sucursal': 'Sucursal',
                    'fecha_contrato': 'Fecha contrato'

                    }
        widgets = {
                    'usuario_id': forms.NumberInput(attrs={
                    'class': 'form-control'
                    }),
                    'run': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombres': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'appaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'apmaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'fecha_nacimiento': forms.DateInput(attrs={
                        'class': 'form-control'
                    }),
                    'genero': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 6
                    }),
                    'email': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'telefono': forms.NumberInput(attrs={
                        'class': 'form-control'
                    }),
                    'nombre_usuario': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'contrasena': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'cod_vendedor': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'sucursal': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'fecha_contrato': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),

    }

class OrdenForm(ModelForm):
    class Meta:
        model = OrdenDeCompra
        fields = ['id' ,'fecha_recepcion' ,'estado' ,'proveedor']

        labels = {
            'fecha_recepcion': 'Fecha Recepcion',
            'estado': 'Estado',
            'proveedor': 'Proveedor'
        }
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={
                    'class': 'form-control',
                    'id': 'datepicker'
                }
            ),
            'estado': forms.Select(attrs={
                    'class': 'form-control'
                }
            ),
            'proveedor': forms.Select(attrs={
                    'class': 'form-control'
                }
            )
        }

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id', 'razon_social', 'sector_comercial', 'direccion', 'email', 'fono']

        labels = {
            'razon_social': 'Razon Social',
            'sector_comercial': 'Sector Comercial',
            'direccion': 'Direccion',
            'email': 'Correo',
            'fono': 'Telefono'
        }
        widgets = {
            'razon_social': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
            'sector_comercial': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
            'direccion': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
            'email': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
            'fono': forms.TextInput(attrs={
                    'class': 'form-control'
                })
        }

class ProductoOrdenForm(ModelForm):
    class Meta:
        model = ProductoOc
        fields = ['producto', 'orden_de_compra', 'cantidad']

        label = {
            'producto': 'Producto',
            'orden_de_compra': 'Orden de compra',
            'cantidad': 'Cantidad'
        }

        widgets = {
            'producto': forms.Select(attrs={
                    'class': 'form-control'
                }),
            'orden_de_compra': forms.TextInput(attrs={
                    'class': 'form-control'
                }),
            'cantidad': forms.TextInput(attrs={
                    'class': 'form-control'
                })
        }

class CrearUsuarioForm(ModelForm):
    opciones_genero=[
        ('M','Masculino'),
        ('F','Femenino'),
        ('N','Prefiero no decir')
    ]
    genero = forms.ChoiceField(
        choices=opciones_genero
    )
    class Meta:
        model = Cliente
        fields = ['run', 'nombres', 'appaterno', 'apmaterno', 'fecha_nacimiento',
                    'genero', 'email', 'telefono',
                    'nombre_usuario', 'contrasena', 'direccion']
        required = [
                    'run',
                    'nombres',
                    'appaterno',
                    'apmaterno',
                    'fecha_nacimiento',
                    'genero',
                    'email',
                    'telefono',
                    'nombre_usuario',
                    'contrasena',
                    'direccion'
        ]
        labels = {  
                    'run': 'run',
                    'nombres': 'Nombres',
                    'appaterno': 'Apellido paterno',
                    'apmaterno': 'Apellido materno',
                    'fecha_nacimiento': 'Fecha nacimiento',
                    'genero': 'Genero',
                    'email': 'Email',
                    'telefono': 'Telefono',
                    'nombre_usuario': 'Nombre usuario',
                    'contrasena': 'Contrasena',
                    'direccion': 'Direccion'
                    }

        widgets = {
                    'run': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 12
                    }),
                    'nombres': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'appaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'apmaterno': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'fecha_nacimiento': forms.DateInput(attrs={
                        'class': 'form-control',
                        'id': 'datepicker'
                    }),
                    'genero': forms.RadioSelect(attrs={
                        'class': 'form-control'
                    }),
                    'email': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'telefono': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                    'nombre_usuario': forms.TextInput(attrs={
                        'class': 'form-control',
                        'max-length': 50
                    }),
                    'contrasena': forms.PasswordInput(attrs={
                        'class': 'form-control'
                    }),
                    'direccion': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
        }
    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        contrasena = self.cleaned_data.get('contrasena')
        if contrasena != confirm:
            raise forms.ValidationError("WOPS")
        return contrasena


