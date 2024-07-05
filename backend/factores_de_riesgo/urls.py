from django.urls import path
from factores_de_riesgo import views

urlpatterns = [
        path("factores_riesgo_paciente/", views.factores_riesgo_paciente),
        path("factores_riesgo_cerrados_paciente/", views.factores_riesgo_cerrados_paciente),
        path("factor_riesgo/", views.factor_riesgo),
        path("historial_factor_riesgo/", views.historial_factor_riesgo),
        path("factores_riesgo/", views.factores_riesgo)
]
