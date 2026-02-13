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
from gimnasio.forms import MembresiaForm

#Listar membresias 
def Listar_membresia(request):
    nombre ={
        'titulo':'Listado de Membresias',
        'membresias': Membresia.objects.all()
    }
    return render(request,'Membresias/listar.html', nombre)

class MembresiaListView(ListView):
    model = Membresia
    template_name = 'Membresias/listar.html'

 
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
        context['titulo'] = 'Listado de membresias'
        context['crear_url']= reverse_lazy('gimnasio:crear_membresias')
        return context


class MembresiaCreateView(CreateView):
    model = Membresia
    template_name = 'Membresias/crear.html'
    form_class = MembresiaForm
    success_url = reverse_lazy('gimnasio:listar_membresias')
    #@method_decorator(csrf_exempt)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear membresia'
        return super().get_context_data(**kwargs)
    
class MembresiaUpdateView(UpdateView):
    model = Membresia
    template_name = 'Membresias/crear.html'
    success_url = reverse_lazy('gimnasio:listar_membresias')
    form_class = MembresiaForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar membresia'
        context['listar_url'] = reverse_lazy('gimnasio:listar_membresias')
        return super().get_context_data(**kwargs)

class MembresiaDeleteView(DeleteView):
    model = Membresia
    template_name = 'Membresias/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_membresias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar membresia'
        context['listar_url'] = reverse_lazy('gimnasio:listar_membresias')
        return context




    
    
    