from django.urls import path
from gimnasio.views.Asistencias.views import *
from gimnasio.views.Membresias.views import *
from gimnasio.views.Notificaciones.views import *
from gimnasio.views.Encuestas.views import *
from gimnasio.views.Soporte_PQRS.views import *
from gimnasio.views.Reportes_Estadisticas.views import *
from gimnasio.views.Categorias.views import *
from gimnasio.views.Nutriciones.views import *
from gimnasio.views.Rutinas.views import *



app_name = 'gimnasio'
# Encuestas
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
    #path('listar_encuestas/', listar_encuestas, name='listar_encuestas'),
    path('listar_encuestas/', EncuestaListView.as_view(), name='listar_encuestas'),
    path('crear_encuesta/', EncuestaCreateView.as_view(), name='crear_encuesta'),
    path('editar_encuesta/<int:pk>/', EncuestaUpdateView.as_view(), name='editar_encuesta'),
    path('eliminar_encuesta/<int:pk>/', EncuestaDeleteView.as_view(), name='eliminar_encuesta'),

# Soporte_PQRS

    path('listar_Soporte_PQRS/', Soporte_PQRSListView.as_view(), name='listar_Soporte_PQRS'),
    path('crear_Soporte_PQRS/', Soporte_PQRSCreateView.as_view(), name='crear_Soporte_PQRS'),
    path('editar_Soporte_PQRS/<int:pk>/', Soporte_PQRSUpdateView.as_view(), name='editar_Soporte_PQRS'),
    path('eliminar_Soporte_PQRS/<int:pk>/', Soporte_PQRSDeleteView.as_view(), name='eliminar_Soporte_PQRS'),

# Reportes_estadisticas

    path('listar_Reportes_estadisticas/', Reportes_estadisticasListView.as_view(), name='listar_Reportes_estadisticas'),
    path('crear_Reportes_estadisticas/', Reportes_estadisticasCreateView.as_view(), name='crear_Reportes_estadisticas'),
    path('editar_Reportes_estadisticas/<int:pk>/', Reportes_estadisticasUpdateView.as_view(), name='editar_Reportes_estadisticas'),
    path('eliminar_Reportes_estadisticas/<int:pk>/', Reportes_estadisticasDeleteView.as_view(), name='eliminar_Reportes_estadisticas'),


    #Categoria
    path('listar_categorias/', categoriaListView.as_view(), name='listar_categorias'),
    path('crear_categoria/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('editar_categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('eliminar_categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
    
    #Nutricion
    path('listar_nutriciones/', nutricionListView.as_view(), name='listar_nutriciones'),
    path('crear_nutricion/', NutricionCreateView.as_view(), name='crear_nutricion'),
    path('editar_nutricion/<int:pk>/', NutricionUpdateView.as_view(), name='editar_nutricion'),
    path('eliminar_nutricion/<int:pk>/', NutricionDeleteView.as_view(), name='eliminar_nutricion'),
    
    
    #Rutina
    path('listar_rutinas/', rutinaListView.as_view(), name='listar_rutinas'),
    path('crear_rutinas/', RutinaCreateView.as_view(), name='crear_rutina'),
    path('editar_rutinas/<int:pk>/', RutinaUpdateView.as_view(), name='editar_rutina'),
    path('eliminar_rutinas/<int:pk>/', RutinaDeleteView.as_view(), name='eliminar_rutina'),
    

]
