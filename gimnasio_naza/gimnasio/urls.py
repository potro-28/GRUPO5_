from django.urls import path
from gimnasio.views.Encuestas.views import *
from gimnasio.views.Soporte_PQRS.views import *
from gimnasio.views.Reportes_Estadisticas.views import *


app_name = 'gimnasio'
# Encuestas
urlpatterns = [
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

]
