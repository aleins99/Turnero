# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Persona(models.Model):
    id = models.SmallAutoField(primary_key=True)
    numero_documento = models.CharField(unique=True, max_length=16)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20, choices=[(
        'M', 'Masculino'), ('F', 'Femenino'), ('NB', 'No Binario')], null=True, blank=True)
    direccion = models.CharField(max_length=70, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_insercion = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.numero_documento

    class Meta:
        db_table = 'persona'


class Atencion(models.Model):
    id = models.BigAutoField(primary_key=True)
    ci = models.CharField(unique=True, max_length=16)
    PRIORIDADES = (
        (3, '3ra Edad, Embarazadas, Discapacidad'),
        (2, 'Clientes corporativos'),
        (1, 'Clientes personales'),
    )
    prioridad = models.IntegerField(choices=PRIORIDADES, null=True)
    horario_atencion = models.TimeField(default=now)
    espcialidad = models.ForeignKey(
        'Servicio', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ci

    class Meta:
        db_table = 'atencion'


class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(
        'Persona', on_delete=models.CASCADE)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=128)
    distrito_id = models.SmallIntegerField()

    class Meta:
        db_table = 'cliente'


class Servicio(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
