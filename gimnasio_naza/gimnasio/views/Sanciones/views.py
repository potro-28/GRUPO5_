from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gimnasio.models import *
from gimnasio.forms import SancionesForm
from django.contrib import messages

#Listar asistencia 
def Listar_sanciones(request):
    nombre ={
        'titulo':'Listado de Sanciones',
        'sanciones': Sancion.objects.all()
    }
    return render(request,'Sanciones/listar.html', nombre)

class SacionesListView(ListView):
    model = Sancion
    template_name = 'Sanciones/listar.html'
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
        context['titulo'] = 'Listado de sanciones'
        context['crear_url']= reverse_lazy('gimnasio:crear_sancion')
        return context


class SancionesCreateView(CreateView):
    model = Sancion
    template_name = 'Sanciones/crear.html'
    form_class = SancionesForm
    success_url = reverse_lazy('gimnasio:listar_sanciones_clas')

    def form_valid(self, form):
        messages.success(self.request, "La sanción se registró correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear sancion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_sanciones_clas')
        return context
class SancionesUpdateView(UpdateView):
    model = Sancion
    template_name = 'Sanciones/crear.html'
    form_class = SancionesForm
    success_url = reverse_lazy('gimnasio:listar_sanciones_clas')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar sancion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_sanciones_clas')
        return context
class SancionesDeleteView(DeleteView):
    model = Sancion
    template_name = 'Sanciones/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_sanciones_clas')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar sancion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_sanciones_clas')
        return context 