from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from gimnasio.models import *
from gimnasio.forms import NutricionForm
import json

@csrf_exempt
def crear_usuario_ajax(request):
    import json
    from datetime import date

    data = json.loads(request.body)

    usuario = Usuario.objects.create(
        documento=data['documento'],
        nombre_usuario=data['nombre'],
        apellido_usuario=data['apellido'],
        correo_usuario=data['correo'],
        telefono_usuario=data.get('telefono', ''),
        fecha_nacimiento=data.get('fecha_nacimiento', '2000-01-01'),
        peso_usuario=data.get('peso', 0),
        altura_usuario=data.get('altura', 0),
        genero_usuario=data.get('genero', 'M'),
        rol='cliente',
        estado='activo',
        fecha_registro=date.today()
    )

    return JsonResponse({
        'id': usuario.id,
        'nombre': f"{usuario.nombre_usuario} {usuario.apellido_usuario}"
    })



#Listar nutriciones
def listar_nutriciones(request):
    nombre ={
        'titulo':'Listado de Nutriciones',
        'Nutriciones': Nutricion.objects.all()
    }
    return render(request,'Nutricion/listar.html', nombre)

class nutricionListView(ListView):
    model = Nutricion
    template_name = 'Nutricion/listar.html'
    
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
        context['titulo'] = 'Listado de Nutriciones'
        context['crear_url'] = reverse_lazy('gimnasio:crear_nutricion')
        return context
    
#Crear categoria    
class NutricionCreateView(CreateView):
    model = Nutricion
    template_name = 'nutricion/crear.html'
    form_class = NutricionForm
    success_url = reverse_lazy('gimnasio:listar_nutriciones')
    
    
    #@method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nutricion'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Nutricion guardada correctamente")
        return super().form_valid(form)
    
    
class NutricionUpdateView(UpdateView):
    model = Nutricion
    form_class = NutricionForm
    template_name = 'nutricion/crear.html'
    success_url = reverse_lazy('gimnasio:listar_nutriciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Nutricion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_nutriciones')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "La nutricion se editó correctamente")
        return super().form_valid(form)
    
    
class NutricionDeleteView(DeleteView):
    model = Nutricion
    template_name = 'nutricion/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_nutriciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Nutricion'
        context['listar_url'] = reverse_lazy('gimnasio:listar_nutriciones')
        return context

    def form_valid(self, form):
        messages.success(self.request, "La nutricion se eliminó correctamente")
        return super().form_valid(form)