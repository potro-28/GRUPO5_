from django.urls import path


from gimnasio.views.registrovisitantestemporales.views import *
from gimnasio.views.turnosdeentrenadores.views import *
from gimnasio.views.certificacionesinternas.views import *

app_name = 'app'
urlpatterns = [
    path('listar_registrovisitantetemporal/', RegistrovisitantetemporalListView.as_view(), name='listar_registrovisitante'),
    path('crear_registrovisitantetemporal/', RegistrovisitantestemporalCreateView.as_view(), name='crear_registrovisitante'),
    path('editar_registrovisitantetemporal/<int:pk>/', RegistrovisitantetemporalUpdateView.as_view(), name='editar_registrovisitante'),
    path('eliminar_registrovisitantetemporal/<int:pk>/', RegistrovisitantetemporalDeleteView.as_view(), name='eliminar_registrovisitante'),
    
    path('listar_turnodeentrenador/', TurnodeentrenadorListView.as_view(), name='listar_turnodeentrenador'),
    path('crear_turnodeentrenador/', TurnodeentrenadorCreateView.as_view(), name='crear_turnodeentrenador'),
    path('editar_turnodeentrenador/<int:pk>/', TurnodeentrenadorUpdateView.as_view(), name='editar_turnodeentrenador'),
    path('eliminar_turnodeentrenador/<int:pk>/', TurnodeentrenadorDeleteView.as_view(), name='eliminar_turnodeentrenador'),
    
    path('listar_certificacioninterna/', CertificacioninternaListView.as_view(), name='listar_certificacioninterna'),
    path('crear_certificacioninterna/', CertificacioninternaCreateView.as_view(), name='crear_certificacioninterna'),
    path('editar_certificacioninterna/<int:pk>/', CertificacioninternaUpdateView.as_view(), name='editar_certificacioninterna'),
    path('eliminar_certificacioninterna/<int:pk>/', CertificacioninternaDeleteView.as_view(), name='eliminar_certificacioninterna'),
]