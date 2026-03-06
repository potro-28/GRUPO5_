from django.shortcuts import render
from django.views.generic import View
from django.views import View as DjangoView
from django.http import HttpResponse
from gimnasio.models import *
from gimnasio.utils import exportar_pdf, exportar_excel
from datetime import datetime

# ====== VISTAS PARA EXPORTAR REPORTES ======

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
    