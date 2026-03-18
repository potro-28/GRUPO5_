import json
from datetime import timedelta
import django.utils.timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from gimnasio.models import Reportes_estadisticas, Usuario, Asistencia, Membresia, Elemento, Soporte_PQRS, Mantenimiento
from gimnasio.forms import Reportes_estadisticasForm

#Listar Reportes y estadisticas
def listar_Reportes_estadisticas(request):
    nombre ={
        'titulo':'Listado de reportes de estadistica',
        'Reportes_estadisticas': Reportes_estadisticas.objects.all()
    }
    return render(request,'Reportes_estadisticas/listar.html', nombre)


class Reportes_estadisticasListView(ListView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/listar.html'
    
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
        context['titulo'] = 'Listado de reportes de estadistica'
        context['crear_url'] = reverse_lazy('gimnasio:crear_Reportes_estadisticas')
        
        # ---------------------------------------------------------
        # //Grafica de barras 
        # ---------------------------------------------------------
        try:
            labels_estadisticas = [
                'Reportes',
                'Membresías',
                'Asistencias',
                'Elementos',
                'Usuarios'
            ]
            
            datos_estadisticas = [
                Reportes_estadisticas.objects.count(),
                Membresia.objects.count(),
                Asistencia.objects.count(),
                Elemento.objects.count(),
                Usuario.objects.count()
            ]
            
            context['labels_estadisticas'] = json.dumps(labels_estadisticas)
            context['datos_estadisticas'] = json.dumps(datos_estadisticas)
        except Exception as e:
            print("Error obteniendo datos estadísticas:", str(e))
            context['labels_estadisticas'] = json.dumps([])
            context['datos_estadisticas'] = json.dumps([])
        
        # Datos para la gráfica de asistencias (en caso de que se usen)
        hoy = django.utils.timezone.now().date()
        dias_semana = []
        asistencias_semana = []
        
        # Recorremos los últimos 7 días hacia atrás (6, 5, 4, 3, 2, 1, 0)
        for i in range(6, -1, -1):
            fecha = hoy - timedelta(days=i)
            # Formateamos la fecha (ej. "05 Mar")
            dias_semana.append(fecha.strftime('%d %b')) 
            # Contamos cuántas asistencias hubo ese día
            asistencias_dia = Asistencia.objects.filter(fecha_asistencia=fecha).count()
            asistencias_semana.append(asistencias_dia)
            
        # Convertimos las listas a JSON para que JavaScript (Chart.js) pueda leerlas
        context['dias_semana'] = json.dumps(dias_semana)
        context['asistencias_semana'] = json.dumps(asistencias_semana)
        
        # Variables para otros gráficos (si existen en el template)
        context['rutinas_labels'] = json.dumps([])
        context['rutinas_data'] = json.dumps([])
        context['porcentaje_activas'] = 0
        context['porcentaje_inactivas'] = 0
        
        return context

#Crear Reportes_estadisticas  
class Reportes_estadisticasCreateView(CreateView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/crear.html'
    form_class = Reportes_estadisticasForm
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    
    #@method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Reportes y estadisticas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte guardado correctamente")
        return super().form_valid(form)
    
class Reportes_estadisticasUpdateView(UpdateView):
    model = Reportes_estadisticas
    form_class = Reportes_estadisticasForm
    template_name = 'Reporte_Estadistica/crear.html'
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Reportes y estadisticas'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte editado correctamente")
        return super().form_valid(form)


# Eliminar Reportes_estadisticas
class Reportes_estadisticasDeleteView(DeleteView):
    model = Reportes_estadisticas
    template_name = 'Reporte_Estadistica/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Reportes y estadisticas'
        context['listar_url'] = reverse_lazy('gimnasio:listar_Reportes_estadisticas')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Reporte eliminado correctamente")
        return super().form_valid(form)
    

class DashboardView1(TemplateView):
    template_name = 'Reporte_Estadistica/listar.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('gimnasio:listar_categorias')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Llamamos al contexto original
        context = super().get_context_data(**kwargs)
        hoy = django.utils.timezone.now().date()
        context['total_usuarios'] = Usuario.objects.count()
        context['membresias_activas'] = Membresia.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy).count()
        context['total_elementos'] = Elemento.objects.count()
            # -------- MANTENIMIENTOS --------
        context['mant_pendientes'] = Mantenimiento.objects.filter(
            estado='pendiente'
        ).count()

        context['mant_proceso'] = Mantenimiento.objects.filter(
            estado='en proceso'
        ).count()

        context['mant_completados'] = Mantenimiento.objects.filter(
            estado='completado'
        ).count()
        
        # Obtenemos la fecha de hoy
        hoy = django.utils.timezone.now().date()
        fecha_limite = hoy + timedelta(days=7)

        membresias_por_vencer = Membresia.objects.filter(
            fecha_fin__gte=hoy,
            fecha_fin__lte=fecha_limite
        ).select_related('fk_usuario')

        context['membresias_por_vencer'] = membresias_por_vencer
        # ---------------------------------------------------------
        # //KPIs principales//
        # ---------------------------------------------------------
        context['usuarios_activos'] = Usuario.objects.filter(estado='activo').count()
        context['elementos_mantenimiento'] = Mantenimiento.objects.filter(
        estado__in=['pendiente', 'en proceso']).count()
        
        # Membresías vigentes (Iniciaron hoy o antes, y terminan hoy o después)
        membresias_activas = Membresia.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy).count()
        context['membresias_activas'] = membresias_activas

        # ---------------------------------------------------------
        # //Estadisticas generales//
        # ---------------------------------------------------------
        context['total_usuarios'] = Usuario.objects.count()
        context['elementos_activos'] = Elemento.objects.filter(estado='activo').count()
        context['pqrs_pendientes'] = Soporte_PQRS.objects.filter(estado='pendiente').count()

        # ---------------------------------------------------------
        # //ultimos 7 dias asistencias//
        # ---------------------------------------------------------
        dias_semana = []
        asistencias_semana = []
        
        # Recorremos los últimos 7 días hacia atrás (6, 5, 4, 3, 2, 1, 0)
        for i in range(6, -1, -1):
            fecha = hoy - timedelta(days=i)
            # Formateamos la fecha (ej. "05 Mar")
            dias_semana.append(fecha.strftime('%d %b')) 
            # Contamos cuántas asistencias hubo ese día
            asistencias_dia = Asistencia.objects.filter(fecha_asistencia=fecha).count()
            asistencias_semana.append(asistencias_dia)
            
        # Convertimos las listas a JSON para que JavaScript (Chart.js) pueda leerlas
        context['dias_semana'] = json.dumps(dias_semana)
        context['asistencias_semana'] = json.dumps(asistencias_semana)

        # ---------------------------------------------------------
        # //Grafica de barras - Conteo por categorias//
        # ---------------------------------------------------------
        labels_estadisticas = [
            'Reportes',
            'Membresías',
            'Asistencias',
            'Elementos',
            'Usuarios'
        ]
        
        datos_estadisticas = [
            Reportes_estadisticas.objects.count(),
            Membresia.objects.count(),
            Asistencia.objects.count(),
            Elemento.objects.count(),
            Usuario.objects.count()
        ]
        
        context['labels_estadisticas'] = json.dumps(labels_estadisticas)
        context['datos_estadisticas'] = json.dumps(datos_estadisticas)
        
        # Obtenemos el listado de reportes
        context['object_list'] = Reportes_estadisticas.objects.all()

        return context
     