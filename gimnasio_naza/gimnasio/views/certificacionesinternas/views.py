from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gimnasio.models import Certificacion_interna
from gimnasio.forms import CertificacioninternaForm
from django.contrib import messages
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.utils import timezone

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
        print('Aqui')
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

class CertificacioninternaUser(View):
    template_name = 'certificacioninterna/diploma.html'
    def get(self,request,pk,*args,**kwargs):
        certificaciones = get_object_or_404(Certificacion_interna,pk=pk)
        context = {
            'nombre' : certificaciones.fk_Asistencia.fk_membresia.fk_usuario.nombre_usuario,
            'apellido' : certificaciones.fk_Asistencia.fk_membresia.fk_usuario.apellido_usuario,
            'documento' : certificaciones.fk_Asistencia.fk_membresia.fk_usuario.documento,
            'fecha' : certificaciones.fk_Asistencia.fk_membresia.fecha_inicio,
            'fecha_hoy' : timezone.now(),
        }
        print(context)
        html_content = render_to_string(self.template_name,context)
        pdf = HTML(string=html_content,base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = f'attachment;filename="Certificacion_{certificaciones.fk_Asistencia.fk_membresia.fk_usuario.nombre_usuario}_{timezone.now().strftime("%Y-%m-%d")}.pdf"'
        return response
        

        