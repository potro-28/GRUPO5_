from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gimnasio.models import Mantenimiento
from gimnasio.forms import MantenimientoForm, ElementoForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
@csrf_exempt
def crear_elemento_ajax(request):
    import json
    from datetime import date

    data = json.loads(request.body)
    
    elemento = elemento.objects.create(
        nombre_elemento=data['nombre_elemento'],
        serial=data['serial'],
        marca=data['marca'],
        peso_elemento=data['peso_elemento'],
        estado=data['estado'],
        fecha_ingreso=data['fecha_ingreso'],
        categoria=data['categoria'],
        imagen=data['imagen']
    )
        
    
    return JsonResponse({
        'id': elemento.id,
        'nombre': elemento.nombre_elemento,
        'serial': elemento.serial,
        'marca': elemento.marca,
        'peso_elemento': elemento.peso_elemento,
        'estado': elemento.estado,
        'fecha_ingreso': elemento.fecha_ingreso,
        'categoria': elemento.categoria,
        'imagen': elemento.imagen.url if elemento.imagen else None
    })

# HISTORIAL DE MANTENIMIENTO 
class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/listar.html'
    context_object_name = 'mantenimientos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crear_url"] = reverse_lazy('gimnasio:crear_mantenimiento')
        return context
    

# REGISTRAR CORRECTIVO Y PREVENTIVO  
class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/crear.html'
    success_url = reverse_lazy('gimnasio:listar_mantenimiento')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Mantenimiento'
        return context 


# EDITAR
class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/crear.html'
    success_url = reverse_lazy('gimnasio:listar_mantenimiento')

  

# ELIMINAR
class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_mantenimiento')
    
    def crear_imagen_elemento(request):
        if request.method == 'POST':
            form = ElementoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_mantenimientos')
        else:
            form = ElementoForm()
        return render(request, 'crear_mantenimiento.html', {'form': form})
