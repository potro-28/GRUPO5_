from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from gimnasio.models import Turnosentrenadores
from gimnasio.forms import TurnodeentrenadorForm


class TurnodeentrenadorListView(ListView):
    model = Turnosentrenadores
    template_name = 'turnodeentrenador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de turnos de entrenadores'
        context['crear_url'] = reverse_lazy('app:crear_turnodeentrenador')
        return context


class TurnodeentrenadorCreateView(CreateView):
    model = Turnosentrenadores
    form_class = TurnodeentrenadorForm
    template_name = 'turnodeentrenador/crear.html'
    success_url = reverse_lazy('app:listar_turnodeentrenador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Turno Entrenadores'
        return context


class TurnodeentrenadorUpdateView(UpdateView):
    model = Turnosentrenadores
    form_class = TurnodeentrenadorForm
    template_name = 'turnodeentrenador/crear.html'
    success_url = reverse_lazy('app:listar_turnodeentrenador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Turno Entrenadores'
        return context
