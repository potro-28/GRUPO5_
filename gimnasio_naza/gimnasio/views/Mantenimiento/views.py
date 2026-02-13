from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gimnasio.models import Mantenimiento
from gimnasio.forms import MantenimientoForm


# HISTORIAL DE MANTENIMIENTO 
class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/listar3.html'
    context_object_name = 'mantenimientos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crear_url"] = reverse_lazy('gimnasio:crear3_mantenimiento')
        return context
    

# REGISTRAR CORRECTIVO Y PREVENTIVO  
class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/crear3.html'
    success_url = reverse_lazy('gimnasio:listar3_mantenimiento')


# EDITAR
class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/crear3.html'
    success_url = reverse_lazy('gimnasio:listar3_mantenimiento')


# ELIMINAR
class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/eliminar3.html'
    success_url = reverse_lazy('gimnasio:listar3_mantenimiento')
