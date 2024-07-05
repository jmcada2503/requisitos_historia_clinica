from rest_framework import serializers
from factores_de_riesgo.models import *

# Para GET api historial_factores_riesgo
class HistorialCambiosFactoresRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCambiosFactoresRiesgo
        fields = ['id_factor_riesgo', 'estado', 'notas', 'fecha']


# Nested serializer
class FactorRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorRiesgo
        fields = ['id', 'nombre', 'razones', 'descripcion']


# Para GET api factores_riesgo_paciente 
class GetFactoresRiesgoPacienteSerializer(serializers.ModelSerializer):
    factor_riesgo = FactorRiesgoSerializer(read_only=True)

    class Meta:
        model = FactorRiesgoPaciente
        fields = ['id', 'id_paciente', 'factor_riesgo']

# Para GET api factor_riesgo
class GetFactorRiesgoSerializer(serializers.ModelSerializer):
    factor_riesgo = FactorRiesgoSerializer(read_only=True)

    class Meta:
        model = FactorRiesgoPaciente
        fields = ['id', 'id_paciente', 'factor_riesgo', 'estado', 'notas', 'fecha_creacion', 'ultima_actualizacion']

# Para POST api factor_riesgo
class SetFactorRiesgoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorRiesgoPaciente
        fields = ['id', 'id_paciente', 'factor_riesgo', 'estado', 'notas', 'fecha_creacion']

# Para PATCH api factor_riesgo
class UpdateFactorRiesgoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorRiesgoPaciente
        fields = ['id', 'estado', 'notas', 'fecha_creacion']
