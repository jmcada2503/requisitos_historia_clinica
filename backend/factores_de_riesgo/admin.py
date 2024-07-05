from django.contrib import admin
from factores_de_riesgo.models import *

# Register your models here.
admin.site.register(FactorRiesgo)
admin.site.register(FactorRiesgoPaciente)
admin.site.register(HistorialCambiosFactoresRiesgo)
