from django.urls import path
from .views import agregar_paciente, pagina_principal, contacto_servicio

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('agregar_paciente/', agregar_paciente , name='agregar_paciente'),
    path('contacto_servicio/', contacto_servicio, name='contacto_servicio'),
]
