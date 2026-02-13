from django.urls import path
from gimnasio.views.Elementos.views import *
from gimnasio.views.Usuario.views import *

app_name = 'gimnasio'

urlpatterns = [
    # Rutas existentes
    path('registrar/', ElementoCreateView.as_view(), name='crear_elemento'),
    path('listar/', ElementoListView.as_view(), name='listar_elementos'),
    path('modificar_estado/<int:pk>/', ElementoUpdateView.as_view(), name='editar_elemento'),
    path('eliminar/<int:pk>/', ElementoDeleteView.as_view(), name='eliminar_elemento'),
#============================usuario============================#
    path('registrar_usuario/', UsuarioCreateView.as_view(), name='crear_usuario'),
    path('listar2_usuarios/', UsuarioListView.as_view(), name='listar2_usuarios'),
    path('modificar_usuario/<int:pk>/', UsuarioUpdateView.as_view(), name='editar2_usuario'),
    path('eliminar2_usuario/<int:pk>/', UsuarioDeleteView.as_view(), name='eliminar2_usuario'),
    path('asignar_rol/<int:pk>/', UsuarioRolUpdateView.as_view(), name='asignar_rol_usuario'),
]    