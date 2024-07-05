from django.urls import path
from problemas_clinicos import views

urlpatterns = [
        path("problemas_clinicos_paciente/", views.problemas_clinicos_paciente),
        path("problemas_clinicos_cerrados_paciente/", views.problemas_clinicos_cerrados_paciente),
        path("problema_clinico/", views.problema_clinico),
        path("historial_problema_clinico/", views.historial_problema_clinico),
        path("problemas_clinicos/", views.problemas_clinicos)
]
