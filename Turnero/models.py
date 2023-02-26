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


class Distrito(models.Model):
    id = models.SmallAutoField(primary_key=True)
    departamento = models.ForeignKey(
        'Departamento', on_delete=models.CASCADE)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=32)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'distrito'


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


class Rol(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=32)
    activo = models.BooleanField()

    class Meta:
        db_table = 'rol'


class Usuario(models.Model):
    id = models.OneToOneField(
        Persona, on_delete=models.CASCADE, db_column='id', primary_key=True)
    nombre = models.CharField(unique=True, max_length=16)
    clave = models.CharField(max_length=32)
    activo = models.BooleanField()
    persona_id = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_insercion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'usuario'


class AperturaCaja(models.Model):
    id = models.IntegerField(primary_key=True)
    servicio = models.ForeignKey(
        'Servicio', on_delete=models.CASCADE)
    usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_usfecha_uso_inicioo = models.DateTimeField()
    fecha_uso_fin = models.DateTimeField(blank=True, null=True)
    caja = models.ForeignKey('Caja',
                             on_delete=models.CASCADE)
    arqueo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'apertura_caja'


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


class Caja(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nro_caja = models.IntegerField()
    fecha_insercion = models.DateTimeField()
    activo = models.BooleanField()
    fecha_cierre = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'caja'


class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(
        'Persona', on_delete=models.CASCADE)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=128)
    distrito_id = models.SmallIntegerField()

    class Meta:
        db_table = 'cliente'


class ClienteCola(models.Model):
    id = models.IntegerField(primary_key=True)
    prioridad = models.ForeignKey(
        'Prioridad', db_column='prioridad', on_delete=models.CASCADE)
    cola = models.ForeignKey('Cola',
                             on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)
    estado = models.ForeignKey(
        'EstadoCliente', db_column='estado', on_delete=models.CASCADE)
    activo = models.BooleanField()

    class Meta:
        db_table = 'cliente_cola'


class Cola(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    servicio = models.ForeignKey(
        'Servicio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cola'


class Departamento(models.Model):
    id = models.SmallAutoField(primary_key=True)
    pais_is = models.ForeignKey(
        'Pais', db_column='pais_is', on_delete=models.CASCADE)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=16)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'departamento'


class Derivacion(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_cola = models.ForeignKey(
        ClienteCola, on_delete=models.CASCADE)
    cola_inicio = models.ForeignKey(
        Cola, db_column='cola_inicio', on_delete=models.CASCADE, related_name='cola_inicio')
    cola_destino = models.ForeignKey(
        Cola, db_column='cola_destino', on_delete=models.CASCADE, related_name='cola_destino')
    motivo = models.CharField(max_length=30)
    generado_por = models.CharField(max_length=15)

    class Meta:
        db_table = 'derivacion'


class EstadoCliente(models.Model):
    id = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=15)
    codigo = models.SmallIntegerField(unique=True)

    class Meta:
        db_table = 'estado_cliente'


class Nacionalidad(models.Model):
    id = models.SmallAutoField(primary_key=True)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=24)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'nacionalidad'


class Pais(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo_iso2 = models.CharField(max_length=2)
    codigo_iso3 = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=16)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'pais'
        unique_together = (('codigo_iso2', 'codigo_iso3'),)


class Permiso(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=32)
    activo = models.BooleanField()

    class Meta:
        db_table = 'permiso'


class Prioridad(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.SmallIntegerField()
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'prioridad'


class RolPermiso(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    permiso = models.ForeignKey(
        Permiso, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'rol_permiso'


class Servicio(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'


class Sexo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=16)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'sexo'


class TipoDocumento(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=16)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'tipo_documento'


class TipoPersona(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.SmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=16)
    activo = models.BooleanField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=16)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(
        max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'tipo_persona'
