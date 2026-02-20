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
from gimnasio.forms import Reportes_estadisticasForm

#Listar Reportes y estadisticas
def listar_Reportes_estadisticas(request):
    nombre ={
        'titulo':'Listado de reportes de estadistica',
        'Reportes_estadisticas': Reportes_estadisticas.objects.all()
    }
    return render(request,'Reportes_estadisticas/listar.html', nombre)

class Reportes_estadisticasListView(ListView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/listar.html'
    
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
        context['titulo'] = 'Listado de reportes de estadistica'
        context['crear_url'] = reverse_lazy('gimnasio:crear_Reportes_estadisticas')
        return context

#Crear Reportes_estadisticas  
class Reportes_estadisticasCreateView(CreateView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/crear.html'
    form_class = Reportes_estadisticasForm
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    
    #@method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Reportes y estadisticas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte guardado correctamente")
        return super().form_valid(form)
    
class Reportes_estadisticasUpdateView(UpdateView):
    model = Reportes_estadisticas
    form_class = Reportes_estadisticasForm
    template_name = 'Reporte_Estadistica/crear.html'
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Reportes y estadisticas'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte editado correctamente")
        return super().form_valid(form)


# Eliminar Reportes_estadisticas
class Reportes_estadisticasDeleteView(DeleteView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Reportes y estadisticas'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte eliminado correctamente")
        return super().form_valid(form)
    


