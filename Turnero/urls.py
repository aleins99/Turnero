from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('', views.vista, name='home'),
    path('registro/', views.solicitarTurno, name='solicitarTurno'),
    path('Personas/registrar', views.registrarPersona, name='registrarPersona'),
    path('servicios/', views.MostrarServicios.as_view(), name='listarServicios'),
    path('servicios/<servicio_id>/turnos/',
         views.mostrarTurnoServicio, name='listarTurnosServicio'),
    path('servicios/turnos/<pk>/eliminar',
         views.eliminarTurno, name='eliminarTurnoServicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
