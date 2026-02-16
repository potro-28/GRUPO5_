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
    path('crear_nutricion/', NutricionCreateView.as_view(), name='crear_nutricion'),
    path('editar_nutricion/<int:pk>/', NutricionUpdateView.as_view(), name='editar_nutricion'),
    path('eliminar_nutricion/<int:pk>/', NutricionDeleteView.as_view(), name='eliminar_nutricion'),
    
    
    #Rutina
    path('listar_rutinas/', rutinaListView.as_view(), name='listar_rutinas'),
    path('crear_rutinas/', RutinaCreateView.as_view(), name='crear_rutina'),
    path('editar_rutinas/<int:pk>/', RutinaUpdateView.as_view(), name='editar_rutina'),
    path('eliminar_rutinas/<int:pk>/', RutinaDeleteView.as_view(), name='eliminar_rutina'),
    

]