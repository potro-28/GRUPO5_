from django.shortcuts import render, redirect
#from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from gimnasio.models import *
from gimnasio.forms import RutinaForm

#Listar rutinas
def listar_rutinas(request):
    nombre ={
        'titulo':'Listado de Rutinas',
        'categorias': Rutina.objects.all()
    }
    return render(request,'rutina/listar.html', nombre)

class rutinaListView(ListView):
    model = Rutina
    template_name = 'rutina/listar.html'
    
    #METODO DISPATCH
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        #if request.method == 'GET':
            #return redirect('app: listar_categorias')    
        return super().dispatch(request, *args, **kwargs)
    
    #METODO POST
    def post(self, request, *args, **kwargs ):
        return super().post(request, *args, **kwargs)

    
    #METODO GET CONTEXT DATA
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Rutinas'
        return context