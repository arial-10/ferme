from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT) + [
    path('', views.home, name='home'),
    # Rutas modulos de Ferme Admin
    path('ferme-admin/', views.home_admin, name='admin'),
    path('ferme-admin/productos/', views.productos_admin,
         name='productos_admin'),
]
