from django.urls import path
from gimnasio.views.Masa_muscular.views import *
from gimnasio.views.Sanciones.views import *

app_name = 'gimnasio'
urlpatterns = [
    path('listar_masa_corporal_clas/', Masa_corporalListView.as_view(), name='listar_masa_corporal_clas'),
    path('crear_masa_corporal/', Masa_corporalCreateView.as_view(), name='crear_masa_corporal'),
    path('eliminar_masa_corporal/<int:pk>/', Masa_corporalDeleteView.as_view(), name='eliminar_masa_corporal'),
    path('editar_masa_corporal/<int:pk>/', Masa_corporalUpdateView.as_view(), name='editar_masa_corporal'),
    path('listar_sanciones_clas/', SacionesListView.as_view(), name='listar_sanciones_clas'),
    path('crear_sancion/', SancionesCreateView.as_view(), name='crear_sancion'),
    path('eliminar_sancion/<int:pk>/', SancionesDeleteView.as_view(), name='eliminar_sancion'),
    path('editar_sancion/<int:pk>/', SancionesUpdateView.as_view(), name='editar_sancion'),
    
]