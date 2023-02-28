from django.contrib import admin
from .models import *
# Register your models here.
# get all the models from the models.py file
# and register them here
admin.site.register(Atencion)
admin.site.register(Cliente)
admin.site.register(Persona)
admin.site.register(Servicio)

