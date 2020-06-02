from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['producto_id', 'sku', 'nombre', 'color', 'descripcion',
                    'stock', 'stock_critico', 'disponibilidad',
                    'precio_normal', 'precio_oferta', 'marca']
        required = [
                    'producto_id',
                    'stock',
                    'stock_critico',
                    'precio_normal',
                    'precio_oferta',
                    'marca'
        ]
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
                        'max-length': 20
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
