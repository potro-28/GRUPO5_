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
from gimnasio.forms import EncuestaForm
import json
from datetime import date, datetime

def crear_usuario_ajax(request):

    if request.method != "POST":
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)

    
        if not data.get('documento') or not data.get('nombre') or not data.get('apellido') or not data.get('correo'):
            return JsonResponse({'error': 'Faltan campos obligatorios'})

  
        if Usuario.objects.filter(documento=data['documento']).exists():
            return JsonResponse({'error': 'El usuario ya existe'})

    
        if data.get('fecha_nacimiento'):
            fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], "%Y-%m-%d").date()
        else:
            fecha_nacimiento = date(2000, 1, 1)

   
        peso = float(data.get('peso') or 0)
        altura = float(data.get('altura') or 0)

        usuario = Usuario.objects.create(
            documento=data['documento'],
            nombre_usuario=data['nombre'],
            apellido_usuario=data['apellido'],
            correo_usuario=data['correo'],
            telefono_usuario=data.get('telefono', ''),
            fecha_nacimiento=fecha_nacimiento,
            peso_usuario=peso,
            altura_usuario=altura,
            genero_usuario=data.get('genero', 'M'),
            rol='cliente',
            estado='activo',
            fecha_registro=date.today()
        )

        return JsonResponse({
            'id': usuario.id,
            'nombre': f"{usuario.nombre_usuario} {usuario.apellido_usuario}"
        })

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        })
#Listar Encuestas
def listar_Encuestas(request):
    nombre ={
        'titulo':'Listado de Encuestas',
        'encuestas': Encuesta.objects.all()
    }
    return render(request,'Encuesta/listar.html', nombre)

class EncuestaListView(ListView):
    model = Encuesta
    template_name = 'Encuesta/listar.html'
    
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
        context['titulo'] = 'Listado de Encuestas'
        context['crear_url'] = reverse_lazy('gimnasio:crear_encuesta')
        return context

#Crear Encuesta    
class EncuestaCreateView(CreateView):
    model = Encuesta
    template_name = 'Encuesta/crear.html'
    form_class = EncuestaForm
    success_url = reverse_lazy('gimnasio:listar_encuestas')
    
    #@method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Encuesta'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Encuesta guardada correctamente")
        return super().form_valid(form)
    
   
class EncuestaUpdateView(UpdateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'Encuesta/crear.html'
    success_url = reverse_lazy('gimnasio:listar_encuestas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Encuesta'
        context['listar_url'] = reverse_lazy('gimnasio:listar_encuestas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Encuesta editada correctamente")
        return super().form_valid(form)


# Eliminar Encuesta   
class EncuestaDeleteView(DeleteView):
    model = Encuesta
    template_name = 'encuesta/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_encuestas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Encuesta'
        context['listar_url'] = reverse_lazy('gimnasio:listar_encuestas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Encuesta eliminada correctamente")
        return super().form_valid(form)
