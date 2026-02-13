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

#Listar notificaciones 
def Listar_notificaciones(request):
    nombre ={
        'titulo':'Listado de Notificaciones',
        'notificaciones': Notificacion.objects.all()
    }
    return render(request,'Notificaciones/listar.html', nombre)

class NotificacionListView(ListView):
    model = Notificacion
    template_name = 'Notificaciones/listar.html'

 
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
        context['titulo'] = 'Listado de notificaciones'
        context['crear_url']= reverse_lazy('gimnasio:crear_notificaciones')
        return context


class NotificacionCreateView(CreateView):
    model = Notificacion
    template_name = 'Notificaciones/crear.html'
    form_class = NotificacionForm
    success_url = reverse_lazy('gimnasio:listar_notificaciones')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear notificacion'
        return super().get_context_data(**kwargs)
    
class NotificacionUpdateView(UpdateView):
    model = Notificacion
    template_name = 'Notificaciones/crear.html'
    success_url = reverse_lazy('gimnasio:listar_notificaciones')
    form_class = NotificacionForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar notificacion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_notificaciones')
        return super().get_context_data(**kwargs)

class NotificacionDeleteView(DeleteView):
    model = Notificacion
    template_name = 'Notificaciones/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_notificaciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar notificacion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_notificaciones')
        return context




    
    
    