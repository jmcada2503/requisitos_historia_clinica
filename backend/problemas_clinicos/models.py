from django.db import models
from django.contrib.postgres import fields

class ProblemaClinico(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)
    sintomas = models.TextField("Sintomas", default="")
    descripcion = models.TextField("Descripción")

    def __str__(self):
        return self.nombre


ESTADOS = [
        ("detected", "Detectado"),
        ("open", "Abierto"),
        ("edited", "Editado"),
        ("closed", "Cerrado"),
]
class ProblemaClinicoPaciente(models.Model):
    id_paciente = models.IntegerField("ID Paciente")
    problema_clinico = models.ForeignKey(ProblemaClinico, on_delete=models.DO_NOTHING)
    estado = models.CharField("Estado", choices=ESTADOS, max_length=10, default="detected")
    notas = models.TextField("Notas", default="", blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)
    ultima_actualizacion = models.DateTimeField("Ultima actualización", auto_now=True)

    def __str__(self):
        return str(self.id_paciente) + " | " + self.problema_clinico.nombre

class HistorialCambiosProblema(models.Model):
    id_problema_paciente = models.ForeignKey(ProblemaClinicoPaciente, on_delete=models.CASCADE)
    estado = models.CharField("Estado", choices=ESTADOS, max_length=10)
    notas = models.TextField("Notas", default="", blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_problema_paciente) + " | " + self.estado + " | " + self.fecha.strftime("%Y/%m/%d %H:%M:%S")
