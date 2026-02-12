from django.urls import path
from gimnasio.views.Masa_muscular.views import *

app_name = 'gimnasio'
urlpatterns = [
    path('listar_masa_corporal_clas/', Masa_corporalListView.as_view(), name='listar_masa_corporal_clas'),
    path('crear_masa_corporal/', Masa_corporalCreateView.as_view(), name='crear_masa_corporal'),

]