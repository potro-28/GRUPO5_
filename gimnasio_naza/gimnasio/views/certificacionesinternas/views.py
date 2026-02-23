from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gimnasio.models import Certificacion_interna
from gimnasio.forms import CertificacioninternaForm
from django.contrib import messages


class CertificacioninternaListView(ListView):
    model = Certificacion_interna
    template_name = 'certificacioninterna/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de certificaciones internas'
        context['crear_url'] = reverse_lazy(
            'gimnasio:crear_certificacioninterna')
        return context


class CertificacioninternaCreateView(CreateView):
    model = Certificacion_interna
    form_class = CertificacioninternaForm
    template_name = 'certificacioninterna/crear.html'
    success_url = reverse_lazy('gimnasio:listar_certificacioninterna')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear certificación interna'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Certificacion creada correctamente')
        return super().form_valid(form)


class CertificacioninternaUpdateView(UpdateView):
    model = Certificacion_interna
    form_class = CertificacioninternaForm
    template_name = 'certificacioninterna/crear.html'
    success_url = reverse_lazy('gimnasio:listar_certificacioninterna')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar certificación interna'
        return context
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Actualizacion de certificación interna actualizado correctamente')
        return super().form_valid(form)


class CertificacioninternaDeleteView(DeleteView):
    model = Certificacion_interna
    template_name = 'certificacioninterna/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_certificacioninterna')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar certificación interna'
        context['listar_url'] = reverse_lazy(
            'gimnasio:listar_certificacioninterna')
        return context
