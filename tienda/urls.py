from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT) + [
    # URLS Ferme Tiena
    path('', views.home, name='home'),
    #Ruta modulo Inicio Sesion
    path('inicio-sesion/', views.ver_inicio_sesion, name='inicio_sesion'),
    #Ruta modulo Registro/ Portal
    path('registro-usuario/', views.agregar_cliente, name='registro_usuario'),
  
    path('catalogo/', views.catalogo, name='catalogo'),
    # URLS Ferme Admin
    path('ferme-admin/', views.home_admin, name='admin'),
    path('ferme-admin/productos/', views.ver_productos_admin,
         name='productos_admin'),
    path('ferme-admin/obtener-productos/',
         views.obtener_productos_admin, name='obtener_productos'),
    path('ferme-admin/productos/agregar-producto/', views.agregar_producto,
         name='agregar_producto'),
    path('ferme-admin/productos/cancelar', views.cancelar_producto,
         name='cancelar_producto'),
    path('ferme-admin/productos/actualizar/<str:id>', views.actualizar_producto, name='actualizar_producto'),
    path('ferme-admin/productos/eliminar/<str:id>', views.eliminar_producto,
         name='eliminar_producto'),
    path('ferme-empleado/', views.home_empleado, name='empleado'),
  
    # Seccion Clientes
    path('ferme-admin/usuarios/clientes.html', views.ver_clientes_admin,
         name='clientes_admin'),
    path('ferme-admin/usuarios/agregar-clientes/', views.agregar_clientes_admin,
         name='agregar_clientes_admin'),
    path('ferme-admin/obtener-clientes/', views.obtener_clientes_admin, 
         name='obtener_clientes_admin'),

    # Seccion Administrador
    path('ferme-admin/usuarios/administrador.html', views.ver_administrador_admin,
         name='administrador_admin'),
    path('ferme-admin/usuarios/agregar-administrador/', views.agregar_administrador_admin,
         name='agregar_administrador_admin'),
    path('ferme-admin/obtener-administrador/', views.obtener_administrador_admin, 
         name='obtener_administrador_admin'),

    # Seccion Empleado
    path('ferme-admin/usuarios/empleado.html', views.ver_empleado_admin,
         name='empleado_admin'),
    path('ferme-admin/usuarios/agregar-empleado/', views.agregar_empleado_admin,
         name='agregar_empleado_admin'),
    path('ferme-admin/obtener-empleado/', views.obtener_empleado_admin, 
         name='obtener_empleado_admin'),

    # Seccion Vendedor
    path('ferme-admin/usuarios/vendedor.html', views.ver_vendedor_admin,
         name='vendedor_admin'),
    path('ferme-admin/usuarios/agregar-vendedor/', views.agregar_vendedor_admin,
         name='agregar_vendedor_admin'),
    path('ferme-admin/obtener-vendedor/', views.obtener_vendedor_admin, 
         name='obtener_vendedor_admin')
  
    
]
