from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gimnasio.models import Registrovisitantestemporales
from gimnasio.forms import RegistrovisitantetemporalForm
from django.contrib import messages

class RegistrovisitantetemporalListView(ListView):
    model = Registrovisitantestemporales
    template_name = 'registrovisitantetemporal/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de visitantes temporales'
        context['crear_url'] = reverse_lazy('gimnasio:crear_registrovisitante')
        return context


class RegistrovisitantestemporalCreateView(CreateView):
    model = Registrovisitantestemporales
    form_class = RegistrovisitantetemporalForm
    template_name = 'registrovisitantetemporal/crear.html'
    success_url = reverse_lazy('gimnasio:listar_registrovisitante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear registro visitante'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro de visitante creado correctamente')
        return super().form_valid(form)



class RegistrovisitantetemporalUpdateView(UpdateView):
    model = Registrovisitantestemporales
    form_class = RegistrovisitantetemporalForm
    template_name = 'registrovisitantetemporal/crear.html'
    success_url = reverse_lazy('gimnasio:listar_registrovisitante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar registro visitante'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Actualizacion de registro visitante actualizado correctamente')
        return super().form_valid(form)
    
class RegistrovisitantetemporalDeleteView(DeleteView):
    model = Registrovisitantestemporales
    template_name = 'registrovisitantetemporal/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_registrovisitante')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar registro visitante'
        context['listar_url'] = reverse_lazy('gimnasio:listar_registrovisitante')
        return context
