from django.urls import path
from gimnasio.views.Asistencias.views import *
from gimnasio_naza.gimnasio.views.Membresias.views import *
from gimnasio_naza.gimnasio.views.Notificaciones.views import *

app_name = 'gimnasio'
urlpatterns = [
    path('listar_asistencia/', AsistenciaListView.as_view(), name='listar_asistencias'),
    path('crear_asistencia/', AsistenciaCreateView.as_view(), name='crear_asistencias'),
    path('editar_asistencia/<int:pk>/', AsistenciaUpdateView.as_view(), name='editar_asistencias'),
    path('eliminar_asistencia/<int:pk>/', AsistenciaDeleteView.as_view(), name='eliminar_asistencia'),
    
    #Membresias
    path('listar_membresia/', MembresiaListView.as_view(), name='listar_membresia'),
    path('crear_membresia/', MembresiaCreateView.as_view(), name='crear_membresia'),
    path('editar_membresia/<int:pk>/', MembresiaUpdateView.as_view(), name='editar_membresia'),
    path('eliminar_membresia/<int:pk>/', MembresiaDeleteView.as_view(), name='eliminar_membresia'),
    
    #Notificaciones
    path('listar_notificaciones/', NotificacionListView.as_view(), name='listar_notificaciones'),
    path('crear_notificaciones/', NotificacionCreateView.as_view(), name='crear_notificaciones '),
    path('editar_notificaciones/<int:pk>/', NotificacionUpdateView.as_view(), name='editar_notificaciones'),
    path('eliminar_notificaciones/<int:pk>/', NotificacionDeleteView.as_view(), name='eliminar_notificaciones'),

]
