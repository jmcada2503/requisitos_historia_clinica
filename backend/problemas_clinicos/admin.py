from django.contrib import admin
from problemas_clinicos.models import ProblemaClinico, ProblemaClinicoPaciente, HistorialCambiosProblema

# Register your models here.
admin.site.register(ProblemaClinico)
admin.site.register(ProblemaClinicoPaciente)
admin.site.register(HistorialCambiosProblema)
