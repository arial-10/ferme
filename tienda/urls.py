from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT) + [
    # ================== URLS Ferme Tienda =============================
    path('', views.home, name='home'),
    #Ruta modulo Inicio Sesion
    path('inicio-sesion/', views.ver_inicio_sesion, name='inicio_sesion'),
    path('inicio-sesion-admin/', views.ver_inicio_sesion_admin, name='inicio_sesion_admin'),
    path('login/', views.cliente_login, name='cliente_login'),
    #Ruta modulo Mis Ordenes
    path('mis-ordenes/', views.ver_mis_ordenes, name='mis_ordenes'),

    #Modulo Recuperar Contraseña
    path('recuperar-contraseña/', views.recuperar_contrasena_cliente, name='recuperar_contrasena_cliente'),
    path('recuperar-contraseña-admin/', views.recuperar_contrasena_admin, name='recuperar_contrasena_admin'),
    #Ruta modulo Registro/ Portal
    path('registro-usuario/', views.agregar_cliente, name='registro_usuario'),
    #Tipo despacho
    path('tipo-despacho/<str:carro>/', views.tipo_despacho, name='tipo_despacho'),
    path('tipo-despacho/<str:carro>/<str:seleccion_despacho>/', views.tipo_despacho, name='tipo_despacho'), 

    #Pago
    path('pago/', views.pago, name='pago'),
    path('pago/<str:despacho>/', views.pago, name='pago'),

    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/categoria/<str:id>', views.ver_categoria, name='categoria'),
    path('catalogo/detalle/<str:id>', views.detalle_producto, name='detalle_producto'),
    path('catalogo/filtrado', views.filtrar_catalogo, name='filtrado'),
    # ================== URLS Ferme Empleado ===========================
    path('home-empleado/', views.home_empleado, name='home_empleado'),
    path('ferme-empleado/boleta/', views.ver_boleta, name='ver_boleta'),
    path('ferme-empleado/obtener-boleta/', views.obtener_boleta, name='obtener_boleta'),
    path('ferme-empleado/nota-credito/<str:id>', views.nota_credito, name='nota_credito'),
    path('ferme-empleado/nota-credito/', views.agregar_notaCredito, name='agregar_notaCredito'),

    path('cuenta/carro-compras', views.ver_carro, name='carro'),
    path('cuenta/carro-compras/eliminar/<str:id>', views.eliminar_carro, name='eliminar_carro'),
    path('catalogo/detalle/agregar_carro/<str:id>', views.agregar_carro, name='agregar_carro'),
    # ================== URLS Ferme Admin ==============================

    # Seccion Productos
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
    path('ferme-admin/usuarios/actualizar-clientes/<str:id>', views.actualizar_clientes_admin,
         name='actualizar_clientes_admin'),
    path('ferme-admin/usuarios/eliminar-cliente/<str:id>', views.eliminar_cliente_admin,
         name='eliminar_cliente_admin'),
    path('ferme-admin/usuarios/cancelar-cliente', views.cancelar_cliente_admin,
         name='cancelar_cliente_admin'),

    # Seccion Administrador
    path('ferme-admin/usuarios/administrador.html', views.ver_administrador_admin,
         name='administrador_admin'),
    path('ferme-admin/usuarios/agregar-administrador/', views.agregar_administrador_admin,
         name='agregar_administrador_admin'),
    path('ferme-admin/obtener-administrador/', views.obtener_administrador_admin,
         name='obtener_administrador_admin'),
    path('ferme-admin/usuarios/actualizar-admin/<str:id>', views.actualizar_administrador_admin,
         name='actualizar_administrador_admin'),
    path('ferme-admin/usuarios/eliminar-admin/<str:id>', views.eliminar_administrador_admin,
         name='eliminar_administrador_admin'),
    path('ferme-admin/usuarios/cancelar-admin', views.cancelar_administrador_admin,
         name='cancelar_administrador_admin'),

    # Seccion Empleado
    path('ferme-admin/usuarios/empleado.html', views.ver_empleado_admin,
         name='empleado_admin'),
    path('ferme-admin/usuarios/agregar-empleado/', views.agregar_empleado_admin,
         name='agregar_empleado_admin'),
    path('ferme-admin/obtener-empleado/', views.obtener_empleado_admin,
         name='obtener_empleado_admin'),
    path('ferme-admin/usuarios/actualizar-empleado-admin/<str:id>', views.actualizar_empleado_admin,
         name='actualizar_empleado_admin'),  
    path('ferme-admin/usuarios/eliminar-empleado/<str:id>', views.eliminar_empleado_admin,
         name='eliminar_empleado_admin'), 
    path('ferme-admin/usuarios/cancelar-empleado', views.cancelar_empleado_admin,
         name='cancelar_empleado_admin'),

    # Seccion Vendedor
    path('ferme-admin/usuarios/vendedor.html', views.ver_vendedor_admin,
         name='vendedor_admin'),
    path('ferme-admin/usuarios/agregar-vendedor/', views.agregar_vendedor_admin,
         name='agregar_vendedor_admin'),
    path('ferme-admin/obtener-vendedor/', views.obtener_vendedor_admin,
         name='obtener_vendedor_admin'),
    path('ferme-admin/usuarios/actualizar-vendedor/<str:id>', views.actualizar_vendedor_admin,
         name='actualizar_vendedor_admin'),
    path('ferme-admin/usuarios/eliminar-vendedor/<str:id>', views.eliminar_vendedor_admin,
         name='eliminar_vendedor_admin'), 
    path('ferme-admin/usuarios/cancelar-vendedor', views.cancelar_vendedor_admin,
         name='cancelar_vendedor_admin'),

    # Seccion Ordenes de compra
    path('ferme-admin/ordenes', views.administrar_oc, name='oc_admin'),
    path('ferme-admin/ordenes/buscar/', views.buscar_ordenes, name='buscar_ordenes'),
    path('ferme-admin/ordenes/actualizar/<str:id>', views.actualizar_orden, name='actualizar_orden'),
    path('ferme-admin/ordenes/agregar/', views.agregar_orden, name='agregar_orden'),
    path('ferme-admin/ordenes/eliminar/<str:id>', views.eliminar_orden, name='eliminar_orden'),
    path('ferme-admin/ordenes/cancelar', views.cancelar_orden, name='cancelar_orden'),
    path('ferme-admin/ordenes/recibir/<str:id>', views.recibir_orden, name='recibir_orden'),
    path('ferme-admin/ordenes/eliminar_item/<str:id>&<str:idOrden>', views.eliminar_item, name='eliminar_item'),
    path('ferme-admin/ordenes/cancelar_item/<str:id>', views.cancelar_item, name='cancelar_item'),
    path('ferme-admin/ordenes/agregar_item/<str:idOrden>', views.agregar_item, name='agregar_item'),
    
    # Seccion Proveedores
    path('ferme-admin/proveedores', views.administrar_proveedores, name='administrar_proveedores'),
    path('ferme-admin/proveedores/buscar/', views.buscar_proveedores, name='buscar_proveedores'),
    path('ferme-admin/proveedores/actualizar/<str:id>', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('ferme-admin/proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('ferme-admin/proveedores/eliminar/<str:id>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('ferme-admin/proveedores/cancelar', views.cancelar_proveedor, name='cancelar_proveedor'),

    # Seccion Autenticacion de prueba
    path('login-cliente/', views.login_cliente, name='login_cliente'),
    path('logout-cliente/', views.logout_cliente, name='logout_cliente'),
    path('login-admin/', views.login_admin, name='login_admin'),
    path('logout-admin/', views.logout_admin, name='logout_admin'),
    path('registro/', views.registro, name='registro_cliente'),
    path('ferme-admin/registro-admin/', views.registro_admin, name='registro_admin'),

    # Seccion Boletas
    path('ferme-admin/boletas', views.administrar_boletas, name='boleta_admin'),

    # Seccion Reportes
    path('ferme-admin/reporte', views.ver_reporte, name='reporte'),
]
