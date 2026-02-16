from django.urls import path

from gimnasio.views import *


























app_name = 'gimnasio'
# Encuestas
urlpatterns = [
    path('', index, name='index'),
]