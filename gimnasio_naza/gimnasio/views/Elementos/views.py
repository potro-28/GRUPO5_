import json
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gimnasio.models import *
from gimnasio.forms import ElementoForm
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def crear_categoria_ajax(request):
    import json
    from datetime import date

    data = json.loads(request.body)

    categoria = Categoria.objects.create(
        nombre_categoria=data['nombre_categoria'],
        descripcion=data['descripcion']
    )

    return JsonResponse({
        'id': categoria.id,
        'nombre': categoria.nombre_categoria
    })

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
# LISTAR imagenes de elementos
# ==============================

def listar_imagenes_elementos(request):
    imagenes = Elemento.objects.filter(imagen__isnull=False)
    return render(request, 'listar_elementos.html', {'imagenes': imagenes})

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
        context['list_url'] = reverse_lazy('gimnasio:listar_elementos')  # ← corregido: 'listar_elemento' → 'listar_elementos'
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
        context['titulo'] = 'Editar Elemento'
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


# ==============================
# CREAR imagen de elemento
# ==============================

def crear_imagen_elemento(request):
    if request.method == 'POST':
        form = ElementoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_elementos')
    else:
        form = ElementoForm()
    return render(request, 'crear_elemento.html', {'form': form})