from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from problemas_clinicos.models import *
from problemas_clinicos.serializers import *

@api_view(['GET'])
def problemas_clinicos_paciente(request):
    if request.method == 'GET':
        print("Problemas clinicos request:", request.GET.get("id_paciente"))
        if request.GET.get("id_paciente"):
            problemas = ProblemaClinicoPaciente.objects.filter(id_paciente=request.GET.get("id_paciente")).exclude(estado="closed")
        else:
            problemas = ProblemaClinicoPaciente.objects.all().exclude(estado="closed")

        if len(problemas):
            serializer = GetProblemasClinicosPacienteSerializer(problemas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def problemas_clinicos_cerrados_paciente(request):
    if request.method == 'GET':
        print("Problemas clinicos request:", request.GET.get("id_paciente"))
        if request.GET.get("id_paciente"):
            problemas = ProblemaClinicoPaciente.objects.filter(id_paciente=request.GET.get("id_paciente"), estado="closed")
        else:
            problemas = ProblemaClinicoPaciente.objects.filter(estado="closed")

        if len(problemas):
            serializer = GetProblemasClinicosPacienteSerializer(problemas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET", "POST", "PATCH"])
def problema_clinico(request):
    if request.method == "GET":
        if request.GET.get("id"):
            problema = ProblemaClinicoPaciente.objects.get(pk=request.GET.get("id"))
            serializer = GetProblemaClinicoPacienteSerializer(problema)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = SetProblemaClinicoPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            historial_serializer = HistorialCambiosProblemaSerializer(data={
                "id_problema_paciente": serializer.data["id"],
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
            problema = ProblemaClinicoPaciente.objects.get(pk=request.data.get("id"))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateProblemaClinicoPacienteSerializer(problema, data=request.data)
        historial_serializer = HistorialCambiosProblemaSerializer(data={
            "id_problema_paciente": request.data["id"],
            "estado": request.data["estado"],
            "notas": request.data["notas"]
            })
        if serializer.is_valid() and historial_serializer.is_valid() and (problema.estado != request.data.get("estado") or problema.notas != request.data.get("notas")):
            serializer.save()
            historial_serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def historial_problema_clinico(request):
    if request.method == "GET":
        if request.GET.get("id"):
            historial = HistorialCambiosProblema.objects.filter(id_problema_paciente=request.GET.get("id"))
            serializer = HistorialCambiosProblemaSerializer(historial, many=True)
            if len(historial):
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def problemas_clinicos(request):
    if request.method == "GET":
        problemas = ProblemaClinico.objects.all()
        serializer = ProblemaClinicoSerializer(problemas, many=True)
        if len(problemas):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
