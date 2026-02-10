from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gimnasio.models import *
from gimnasio.forms import AsistenciaForm

#Listar asistencia 
def Listar_asistencia(request):
    nombre ={
        'titulo':'Listado de Asistencias',
        'asistencias': Asistencia.objects.all()
    }
    return render(request,'Asistencia/listar.html', nombre)

class AsistenciaListView(ListView):
    model = Asistencia
    template_name = 'Asistencia/listar.html'

 
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
        context['crear_url']= reverse_lazy('app:crear_asistencias')
        return context


class AsistenciaCreateView(CreateView):
    model = Asistencia
    template_name = 'Asistencia/crear.html'
    form_class = AsistenciaForm
    success_url = reverse_lazy('app:listar_asistencias')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear asistencia'
        return super().get_context_data(**kwargs)
    
class AsistenciaUpdateView(UpdateView):
    model = Asistencia
    template_name = 'Asistencia/crear.html'
    success_url = reverse_lazy('app:listar_asistencias')
    form_class = AsistenciaForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Asistencia'
        context['listar_url'] = reverse_lazy('app:listar_asistencias')
        return super().get_context_data(**kwargs)



    
    
    