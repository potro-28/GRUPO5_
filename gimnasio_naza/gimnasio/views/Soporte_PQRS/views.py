from django.shortcuts import render, redirect
#from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages

from gimnasio.models import *
from gimnasio.forms import Soporte_PQRSForm

#Listar Soporte_PQRS
def listar_Soporte_PQRS(request):
    nombre ={
        'titulo':'Listado de Soportes y PQRS',
        'Soporte_PQRS': Soporte_PQRS.objects.all()
    }
    return render(request,'Soporte_PQRS/listar.html', nombre)

class Soporte_PQRSListView(ListView):
    model = Soporte_PQRS
    template_name = 'Soporte_PQR/listar.html'
    
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
        context['titulo'] = 'Listado de Soporte y PQRS'
        context['crear_url'] = reverse_lazy('gimnasio:crear_Soporte_PQRS')
        return context

#Crear Soporte_PQRS   
class Soporte_PQRSCreateView(CreateView):
    model = Soporte_PQRS
    template_name = 'Soporte_PQR/crear.html'
    form_class = Soporte_PQRSForm
    success_url = reverse_lazy('gimnasio:listar_Soporte_PQRS')
    
    
    #@method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Soporte y PQRS'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Soporte guardado correctamente")
        return super().form_valid(form)
    
class Soporte_PQRSUpdateView(UpdateView):
    model = Soporte_PQRS
    form_class = Soporte_PQRSForm
    template_name = 'Soporte_PQR/crear.html'
    success_url = reverse_lazy('gimnasio:listar_Soporte_PQRS')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Soporte y PQRS'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Soporte_PQRS')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Soporte editado correctamente")
        return super().form_valid(form)


# Eliminar Soporte_PQRS  
class Soporte_PQRSDeleteView(DeleteView):
    model = Soporte_PQRS
    template_name = 'Soporte_PQR/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_Soporte_PQRS')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Soporte yPQRS'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Soporte_PQRS')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Soporte eliminado correctamente")
        return super().form_valid(form)
    

