from django.urls import path
from gimnasio.views.Asistencias.views import *
from gimnasio.views.Membresias.views import *
from gimnasio.views.Notificaciones.views import *




































app_name = 'gimnasio'
urlpatterns = [
    path('listar_asistencia/', AsistenciaListView.as_view(), name='listar_asistencia'),
    path('crear_asistencia/', AsistenciaCreateView.as_view(), name='crear_asistencia'),
    path('editar_asistencia/<int:pk>/', AsistenciaUpdateView.as_view(), name='editar_asistencia'),
    path('eliminar_asistencia/<int:pk>/', AsistenciaDeleteView.as_view(), name='eliminar_asistencia'),
    
    #Membresias
    path('listar_membresia/', MembresiaListView.as_view(), name='listar_membresia'),
    path('crear_membresia/', MembresiaCreateView.as_view(), name='crear_membresia'),
    path('editar_membresia/<int:pk>/', MembresiaUpdateView.as_view(), name='editar_membresia'),
    path('eliminar_membresia/<int:pk>/', MembresiaDeleteView.as_view(), name='eliminar_membresia'),
    
    #Notificaciones
    path('listar_notificacion/', NotificacionListView.as_view(), name='listar_notificacion'),
    path('crear_notificacion/', NotificacionCreateView.as_view(), name='crear_notificacion'),
    path('editar_notificacion/<int:pk>/', NotificacionUpdateView.as_view(), name='editar_notificacion'),
    path('eliminar_notificacion/<int:pk>/', NotificacionDeleteView.as_view(), name='eliminar_notificacion'),

]
