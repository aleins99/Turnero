from django.contrib import admin
from .models import *
# Register your models here.
# get all the models from the models.py file
# and register them here
admin.site.register(AperturaCaja)
admin.site.register(Atencion)
admin.site.register(Caja)
admin.site.register(Cliente)
admin.site.register(ClienteCola)
admin.site.register(Cola)
admin.site.register(Departamento)
admin.site.register(Derivacion)
admin.site.register(Distrito)
admin.site.register(EstadoCliente)
admin.site.register(Nacionalidad)
admin.site.register(Pais)
admin.site.register(Permiso)
admin.site.register(Persona)
admin.site.register(Prioridad)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Servicio)
admin.site.register(Sexo)
admin.site.register(TipoDocumento)
admin.site.register(TipoPersona)
admin.site.register(Usuario)
