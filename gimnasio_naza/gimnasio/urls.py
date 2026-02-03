from django.urls import path

from gimnasio.views import *

app_name = 'gimnasio'
urlpatterns = [
    path('', index, name='index'),
]