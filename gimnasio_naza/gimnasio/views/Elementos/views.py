from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gimnasio.models import Elemento
from gimnasio.forms import ElementoForm
# ==============================
# LISTAR ELEMENTOS
# ==============================

class ElementoListView(ListView):
    model = Elemento
    template_name = 'elementos/listar.html'
    context_object_name = 'elementos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Elementos'
        context['crear_url'] = reverse_lazy('gimnasio:crear_elemento')
        return context


# ==============================
# REGISTRAR ELEMENTO
# ==============================

class ElementoCreateView(CreateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'elementos/crear.html'
    success_url = reverse_lazy('gimnasio:listar_elementos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar Elemento'
        context['list_url'] = reverse_lazy('gimnasio:listar_elementos')
        return context


# ==============================
# MODIFICAR ESTADO
# ==============================

class ElementoUpdateView(UpdateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'elementos/crear.html'
    success_url = reverse_lazy('gimnasio:listar_elementos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'editar_elementoo'
        context['list_url'] = reverse_lazy('gimnasio:listar_elementos')
        return context


# ==============================
# ELIMINAR ELEMENTO
# ==============================

class ElementoDeleteView(DeleteView):
    model = Elemento
    template_name = 'elementos/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_elementos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Elemento'
        context['list_url'] = reverse_lazy('gimnasio:listar_elementos')
        return context
#=============================
#GESTION DE USUARIOS
#=============================
