from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT) + [
    path('', views.home, name='home'),
    # Rutas modulos de Ferme Admin
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
    path('ferme-admin/productos/actualizar/<str:id>', views.actualizar_producto,
         name='actualizar_producto'),
    path('ferme-admin/productos/eliminar/<str:id>', views.eliminar_producto,
         name='eliminar_producto')
]
