from django.urls import path
from gimnasio.views.Categorias.views import *
from gimnasio.views.Nutriciones.views import *
from gimnasio.views.Rutinas.views import *



app_name = 'gimnasio'
urlpatterns = [
    #Categoria
    path('listar_categorias/', categoriaListView.as_view(), name='listar_categorias'),
    path('crear_categoria/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('editar_categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('eliminar_categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
    
    #Nutricion
    path('listar_nutriciones/', nutricionListView.as_view(), name='listar_nutriciones'),
    
    #Rutina
    path('listar_rutinas/', rutinaListView.as_view(), name='listar_rutinas'),

]