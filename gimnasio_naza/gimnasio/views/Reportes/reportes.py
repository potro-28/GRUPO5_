from django.shortcuts import render
from django.views.generic import View
from django.views import View as DjangoView
from django.http import HttpResponse
from gimnasio.models import *
from gimnasio.utils import exportar_pdf, exportar_excel
from datetime import datetime

# ====== VISTAS PARA EXPORTAR REPORTES ======

class ExportarAsistenciaPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A PDF
    Obtiene todas las categorías y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        asistencia = Asistencia.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID','Fecha de asistencia','Hora de ingreso','Hora de salida','Membresia','Documento de usuario']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (a.id,a.fecha_asistencia,a.hora_ingreso,a.hora_salida,(a.fk_membresia.fk_usuario.nombre_usuario,a.fk_membresia.fk_usuario.apellido_usuario),a.fk_membresia.fk_usuario.documento)
            for a in asistencia
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Asistencia_{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE ASISTENCIAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarAsistenciaExcel(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        asistencia = Asistencia.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID', 'Fecha de asistencia', 'Hora de ingreso', 'Hora de salida', 'Membresia','Documento de usuario']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (a.id,a.fecha_asistencia,a.hora_ingreso,a.hora_salida,(a.fk_membresia.fk_usuario.nombre_usuario,a.fk_membresia.fk_usuario.apellido_usuario),a.fk_membresia.fk_usuario.documento)
            for a in asistencia
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Asistencia_{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_excel(
            titulo='REPORTE DE ASISTENCIAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


# ====== VISTAS PARA EXPORTAR REPORTES MEMBRESIA======

class ExportarMembresiaPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A PDF
    Obtiene todas las categorías y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        membresia = Membresia.objects.all()
        
        # Definir las columnas que se 
        # 
        # en el reporte
        columnas = ['ID','Fecha de inicio','Fecha de fin','Membresia','Documento de usuario']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (m.id,m.fecha_inicio, m.fecha_fin,(m.fk_usuario.nombre_usuario,m.fk_usuario.apellido_usuario),m.fk_usuario.documento)
            for m in membresia
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_membresia_{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE MEMBRESIAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarMembresiaExcel(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        membresia = Membresia.objects.all()
        
        # Definir las columnas que se 
        # 
        # en el reporte
        columnas = ['ID','Fecha de inicio','Fecha de fin','Membresia','Documento de usuario']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (m.id,m.fecha_inicio, m.fecha_fin,(m.fk_usuario.nombre_usuario,m.fk_usuario.apellido_usuario),m.fk_usuario.documento)
            for m in membresia
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_membresia_{datetime.now().strftime("%d_%m_%Y")}'    
        
        # Llamar funcion de exportacion a PDF
        return exportar_excel(
            titulo='REPORTE DE MEMBRESIAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )



























































































































































































































































































































































class ExportarReportes_estadisticasPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A PDF
    Obtiene todas las categorías y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        reportes = Reportes_estadisticas.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID', 'Tipo Reporte', 'Fecha Generacion']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (rep.id, rep.tipo_reporte, rep.fecha_generacion)
            for rep in reportes
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reportes_Estadisticas{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE Y ESTADISTICAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarReportes_estadisticasEXCEL(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        reportes = Reportes_estadisticas.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Tipo Reporte', 'Fecha Generacion']
        
        # Preparar los datos en  tuplas
        datos = [
            (rep.id, rep.tipo_reporte, rep.fecha_generacion)
            for rep in reportes
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reportes_estadisticas{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE Y ESTADISTICAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )

# ====== VISTAS PARA EXPORTAR SOPORTES Y PQRS ======

class ExportarSoporte_PQRSPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A PDF
    Obtiene todas las categorías y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        soportes = Soporte_PQRS.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID','Tipo', 'Descripcion', 'Fecha Ingreso', 'Estado']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (soporte.id, soporte.tipo, soporte.descripcion, soporte.fecha_ingreso, soporte.estado)
            for soporte in soportes
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Soporte_PQRS{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='SOPORTE Y PQRS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarSoporte_PQRSEXCEL(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        soportes = Soporte_PQRS.objects.all()
        
        # Definir las columnas que se muestran en el soporte y pqr
        columnas = ['ID','Tipo', 'Descripcion', 'Fecha Ingreso', 'Estado']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (soporte.id, soporte.tipo, soporte.descripcion, soporte.fecha_ingreso, soporte.estado)
            for soporte in soportes
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Soporte_PQRS{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='SOPORTE Y PQRS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )   
        
        