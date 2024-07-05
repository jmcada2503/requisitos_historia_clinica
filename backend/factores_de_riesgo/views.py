from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from factores_de_riesgo.models import *
from factores_de_riesgo.serializers import *

@api_view(['GET'])
def factores_riesgo_paciente(request):
    if request.method == 'GET':
        if request.GET.get("id_paciente"):
            factores_riesgo = FactorRiesgoPaciente.objects.filter(id_paciente=request.GET.get("id_paciente")).exclude(estado="closed")
        else:
            factores_riesgo = FactorRiesgoPaciente.objects.all().exclude(estado="closed")

        if len(factores_riesgo):
            serializer = GetFactoresRiesgoPacienteSerializer(factores_riesgo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def factores_riesgo_cerrados_paciente(request):
    if request.method == 'GET':
        if request.GET.get("id_paciente"):
            factores_riesgo = FactorRiesgoPaciente.objects.filter(id_paciente=request.GET.get("id_paciente"), estado="closed")
        else:
            factores_riesgo = FactorRiesgoPaciente.objects.filter(estado="closed")

        if len(factores_riesgo):
            serializer = GetFactoresRiesgoPacienteSerializer(factores_riesgo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET", "POST", "PATCH"])
def factor_riesgo(request):
    if request.method == "GET":
        if request.GET.get("id"):
            factor_riesgo = FactorRiesgoPaciente.objects.get(pk=request.GET.get("id"))
            serializer = GetFactorRiesgoSerializer(factor_riesgo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = SetFactorRiesgoPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            historial_serializer = HistorialCambiosFactoresRiesgoSerializer(data={
                "id_factor_riesgo": serializer.data["id"],
                "estado": serializer.data["estado"],
                "notas": serializer.data["notas"]
            })
            if historial_serializer.is_valid():
                historial_serializer.save()
            else:
                print(historial_serializer.errors)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        try:
            factor_riesgo = FactorRiesgoPaciente.objects.get(pk=request.data.get("id"))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateFactorRiesgoPacienteSerializer(factor_riesgo, data=request.data)
        historial_serializer = HistorialCambiosFactoresRiesgoSerializer(data={
            "id_factor_riesgo": request.data["id"],
            "estado": request.data["estado"],
            "notas": request.data["notas"]
            })
        if serializer.is_valid() and historial_serializer.is_valid() and (factor_riesgo.estado != request.data.get("estado") or factor_riesgo.notas != request.data.get("notas")):
            serializer.save()
            historial_serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def historial_factor_riesgo(request):
    if request.method == "GET":
        if request.GET.get("id"):
            historial = HistorialCambiosFactoresRiesgo.objects.filter(id_factor_riesgo=request.GET.get("id"))
            serializer = HistorialCambiosFactoresRiesgoSerializer(historial, many=True)
            if len(historial):
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def factores_riesgo(request):
    if request.method == "GET":
        factores_riesgo = FactorRiesgo.objects.all()
        serializer = FactorRiesgoSerializer(factores_riesgo, many=True)
        if len(factores_riesgo):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
