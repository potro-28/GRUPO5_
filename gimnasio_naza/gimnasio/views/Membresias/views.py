import json
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gimnasio.models import Membresia
from gimnasio.forms import MembresiaForm


class MembresiaListView(ListView):
    model = Membresia
    template_name = 'Membresia/listar.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de membresias'
        context['crear_url'] = reverse_lazy('gimnasio:crear_membresia')

        # // LOGICA PARA EL GRAFICO ///
        hoy = timezone.now().date()
        
        # Calculamos los estados
        activas = Membresia.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy).count()
        vencidas = Membresia.objects.filter(fecha_fin__lt=hoy).count()
        
        
        context['total_membresias'] = activas + vencidas 
        
        # Empaquetamos en JSON para Chart.js
        context['chart_labels'] = json.dumps(['Activas', 'Vencidas'])
        context['chart_data'] = json.dumps([activas, vencidas])
        
        return context

class MembresiaCreateView(CreateView):
    model = Membresia
    template_name = 'Membresia/crear.html'
    form_class = MembresiaForm
    success_url = reverse_lazy('gimnasio:listar_membresia')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear membresia'
        return context
    
class MembresiaUpdateView(UpdateView):
    model = Membresia
    template_name = 'Membresia/crear.html'
    success_url = reverse_lazy('gimnasio:listar_membresia')
    form_class = MembresiaForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar membresia'
        context['listar_url'] = reverse_lazy('gimnasio:listar_membresia')
        return context

class MembresiaDeleteView(DeleteView):
    model = Membresia
    template_name = 'Membresia/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_membresia')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar membresia'
        context['listar_url'] = reverse_lazy('gimnasio:listar_membresia')
        return context