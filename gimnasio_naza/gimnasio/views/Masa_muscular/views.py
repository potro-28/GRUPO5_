from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gimnasio.models import *
from gimnasio.forms import Masa_muscularForm

#Listar asistencia 
def Listar_masa_corporal(request):
    nombre ={
        'titulo':'Listado de Masa Muscular',
        'masa_muscular': Masa_corporal.objects.all()
    }
    return render(request,'Masa_muscular/listar.html', nombre)

class Masa_corporalListView(ListView):
    model = Masa_corporal
    template_name = 'Masa_muscular/listar.html'
    # metodo dispatch
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        #if request.method == 'GET':
            #return redirect('app:listar_categorias')
        return super().dispatch(request, *args, **kwargs)
    
    # metodo post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    #metodo context data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de asistencias'
        context['crear_url']= reverse_lazy('gimnasio:crear_asistencias')
        return context


class Masa_corporalCreateView(CreateView):
    model = Masa_corporal
    template_name = 'masa_muscular/crear.html'
    form_class = Masa_muscularForm
    success_url = reverse_lazy('gimnasio:listar_masa_corporal_clas')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear masa corporal'
        return context
    
