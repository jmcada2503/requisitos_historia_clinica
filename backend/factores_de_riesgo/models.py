from django.db import models
from django.contrib.postgres import fields

class FactorRiesgo(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)
    razones = models.TextField("Razones", default="")
    descripcion = models.TextField("Descripción")

    def __str__(self):
        return self.nombre


ESTADOS = [
        ("detected", "Detectado"),
        ("open", "Abierto"),
        ("edited", "Editado"),
        ("closed", "Cerrado"),
]
class FactorRiesgoPaciente(models.Model):
    id_paciente = models.IntegerField("ID Paciente")
    factor_riesgo = models.ForeignKey(FactorRiesgo, on_delete=models.DO_NOTHING)
    estado = models.CharField("Estado", choices=ESTADOS, max_length=10, default="detected")
    notas = models.TextField("Notas", default="", blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)
    ultima_actualizacion = models.DateTimeField("Ultima actualización", auto_now=True)

    def __str__(self):
        return str(self.id_paciente) + " | " + self.factor_riesgo.nombre

class HistorialCambiosFactoresRiesgo(models.Model):
    id_factor_riesgo = models.ForeignKey(FactorRiesgoPaciente, on_delete=models.CASCADE)
    estado = models.CharField("Estado", choices=ESTADOS, max_length=10)
    notas = models.TextField("Notas", default="", blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_factor_riesgo) + " | " + self.estado + " | " + self.fecha.strftime("%Y/%m/%d %H:%M:%S")
