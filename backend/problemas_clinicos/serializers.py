from rest_framework import serializers
from problemas_clinicos.models import *

class HistorialCambiosProblemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCambiosProblema
        fields = ['id_problema_paciente', 'estado', 'notas', 'fecha']


class ProblemaClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemaClinico
        fields = ['id', 'nombre', 'sintomas', 'descripcion']


# Para GET api problemas_clinicos_paciente 
class GetProblemasClinicosPacienteSerializer(serializers.ModelSerializer):
    problema_clinico = ProblemaClinicoSerializer(read_only=True)

    class Meta:
        model = ProblemaClinicoPaciente
        fields = ['id', 'id_paciente', 'problema_clinico']

# Para GET api problema_clinico
class GetProblemaClinicoPacienteSerializer(serializers.ModelSerializer):
    problema_clinico = ProblemaClinicoSerializer(read_only=True)

    class Meta:
        model = ProblemaClinicoPaciente
        fields = ['id', 'id_paciente', 'problema_clinico', 'estado', 'notas', 'fecha_creacion', 'ultima_actualizacion']

# Para POST api problema_clinico
class SetProblemaClinicoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemaClinicoPaciente
        fields = ['id', 'id_paciente', 'problema_clinico', 'estado', 'notas', 'fecha_creacion']

# Para PATCH api problema_clinico
class UpdateProblemaClinicoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemaClinicoPaciente
        fields = ['id', 'estado', 'notas', 'fecha_creacion']
