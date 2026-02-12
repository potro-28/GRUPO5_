from django.urls import path
from gimnasio.views.Asistencias.views import *

app_name = 'gimnasio'
urlpatterns = [
    path('listar_asistencia/', AsistenciaListView.as_view(), name='listar_asistencias'),
    path('crear_asistencia/', AsistenciaCreateView.as_view(), name='crear_asistencias'),
    path('editar_asistencia/<int:pk>/', AsistenciaUpdateView.as_view(), name='editar_asistencias'),
    path('eliminar_asistencia/<int:pk>/', AsistenciaDeleteView.as_view(), name='eliminar_asistencia'),

]
