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
from gimnasio.utils import crear_formulario_google, actualizar_formulario_google, obtener_formulario_google
import json
from django.utils import timezone
from datetime import date, datetime

from django.core.mail import send_mail
from django.conf import settings

def enviar_encuesta_usuarios(request):
    if request.method == 'POST':
        encuesta_id = request.POST.get('encuesta_id')
        usuarios_ids = request.POST.getlist('usuarios')
        
        if not encuesta_id or not usuarios_ids:
            messages.error(request, "Debe seleccionar una encuesta y al menos un usuario.")
            return redirect('gimnasio:listar_encuestas')
        
        try:
            encuesta = Encuesta.objects.get(id=encuesta_id)
            usuarios = Usuario.objects.filter(id__in=usuarios_ids)
            
            if not encuesta.form_id:
                messages.error(request, "La encuesta no tiene un formulario de Google Forms asociado.")
                return redirect('gimnasio:listar_encuestas')
            
            # Generar link del formulario
            form_link = f"https://docs.google.com/forms/d/{encuesta.form_id}/viewform"
            
            # Enviar emails
            for usuario in usuarios:
                if usuario.correo_usuario:
                    subject = f"Encuesta: {encuesta.nombre}"
                    message = f"""
                    Hola {usuario.nombre_usuario},

                    Te invitamos a participar en la siguiente encuesta: {encuesta.nombre}

                    Link: {form_link}

                    Gracias por tu participación.
                    """
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [usuario.correo_usuario])
            
            # Marcar fecha de envío
            encuesta.fecha_envio = timezone.now()
            encuesta.save()
            
            messages.success(request, f"Encuesta enviada a {len(usuarios)} usuarios.")
        except Encuesta.DoesNotExist:
            messages.error(request, "Encuesta no encontrada.")
        except Exception as e:
            messages.error(request, f"Error al enviar la encuesta: {str(e)}")
    
    return redirect('gimnasio:listar_encuestas')


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


def enviar_encuesta(request, pk):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if not usuario_id:
            messages.error(request, "Debes seleccionar un usuario para enviar la encuesta.")
            return redirect('gimnasio:listar_encuestas')

        try:
            encuesta = Encuesta.objects.get(pk=pk)
            usuario = Usuario.objects.get(pk=usuario_id)

            if not encuesta.form_id:
                messages.error(request, "La encuesta no tiene un formulario de Google Forms asociado.")
                return redirect('gimnasio:listar_encuestas')

            form_link = f"https://docs.google.com/forms/d/{encuesta.form_id}/viewform"
            subject = f"Encuesta: {encuesta.nombre}"
            message = f"""
Hola {usuario.nombre_usuario},

Te invitamos a participar en la siguiente encuesta: {encuesta.nombre}

Link: {form_link}

Gracias por tu participación.
"""
            if usuario.correo_usuario:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [usuario.correo_usuario])

            encuesta.fecha_envio = timezone.now()
            encuesta.save()
            messages.success(request, f"Encuesta enviada a {usuario.nombre_usuario} {usuario.apellido_usuario}.")
        except Encuesta.DoesNotExist:
            messages.error(request, "Encuesta no encontrada.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al enviar la encuesta: {str(e)}")
    return redirect('gimnasio:listar_encuestas')

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
        context['usuarios_activos'] = Usuario.objects.filter(estado='activo')
        return context

from gimnasio.forms import EncuestaForm, PreguntaFormSet

#Crear Encuesta    
def crear_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        formset = PreguntaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            # Crear el formulario en Google Forms
            try:
                google_form = crear_formulario_google(form.cleaned_data['nombre'], "Encuesta personalizada del gimnasio")
                form_id = google_form['formId']
            except Exception as e:
                messages.warning(request, f"Encuesta guardada, pero error al crear formulario Google: {str(e)}")
                form_id = None
            
            encuesta = form.save(commit=False)
            encuesta.form_id = form_id
            encuesta.save()
            form.save_m2m()
            
            # Guardar preguntas y agregar a Google Form
            if form_id:
                try:
                    agregar_preguntas_a_formulario(form_id, formset)
                except Exception as e:
                    messages.warning(request, f"Error al agregar preguntas al formulario: {str(e)}")
            
            formset.instance = encuesta
            formset.save()
            
            messages.success(request, "Encuesta guardada correctamente")
            return redirect('gimnasio:listar_encuestas')
    else:
        form = EncuestaForm()
        formset = PreguntaFormSet()
    
    return render(request, 'Encuesta/crear.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Crear Encuesta'
    })

class EncuestaUpdateView(UpdateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'Encuesta/crear.html'
    success_url = reverse_lazy('gimnasio:listar_encuestas')
    
   
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
        response = super().form_valid(form)
        
        # Actualizar miembros
        if 'miembros' in form.cleaned_data:
            self.object.miembros.set(form.cleaned_data['miembros'])
        
        # Si hay form_id, actualizar el título en Google Forms
        if self.object.form_id:
            try:
                updates = {
                    "requests": [
                        {
                            "updateFormInfo": {
                                "info": {
                                    "title": self.object.nombre
                                },
                                "updateMask": "title"
                            }
                        }
                    ]
                }
                actualizar_formulario_google(self.object.form_id, updates)
            except Exception as e:
                messages.warning(self.request, f"Error al actualizar formulario Google: {str(e)}")
        
        messages.success(self.request, "Encuesta editada correctamente")
        return response


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
