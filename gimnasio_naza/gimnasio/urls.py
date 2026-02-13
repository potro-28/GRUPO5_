from django.urls import path
from gimnasio.views.Elementos.views import *
from gimnasio.views.Usuario.views import *
from gimnasio.views.Mantenimiento.views import *

app_name = 'gimnasio'

urlpatterns = [
    # Rutas existentes
    path('crear/', ElementoCreateView.as_view(), name='crear_elemento'),
    path('listar/', ElementoListView.as_view(), name='listar_elementos'),
    path('modificar_estado/<int:pk>/', ElementoUpdateView.as_view(), name='editar_elemento'),
    path('eliminar/<int:pk>/', ElementoDeleteView.as_view(), name='eliminar_elemento'),
#============================usuario============================#
    path('crear_usuario/', UsuarioCreateView.as_view(), name='crear2_usuario'),
    path('listar2_usuarios/', UsuarioListView.as_view(), name='listar2_usuarios'),
    path('modificar_usuario/<int:pk>/', UsuarioUpdateView.as_view(), name='editar2_usuario'),
    path('eliminar2_usuario/<int:pk>/', UsuarioDeleteView.as_view(), name='eliminar2_usuario'),
    path('asignar_rol/<int:pk>/', UsuarioRolUpdateView.as_view(), name='asignar_rol_usuario'),
#==============================mantenimiento==============================#
    path('crear_mantenimiento/', MantenimientoCreateView.as_view(), name='crear3_mantenimiento'),
    path('listar3_mantenimiento/', MantenimientoListView.as_view(), name='listar3_mantenimiento'),
    path('modificar_mantenimiento/<int:pk>/', MantenimientoUpdateView.as_view(), name='editar3_mantenimiento'),
    path('eliminar_mantenimiento/<int:pk>/', MantenimientoDeleteView.as_view(), name='eliminar3_mantenimiento'),
]    