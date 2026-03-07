from django.shortcuts import render
from django.views.generic import View
from django.views import View as DjangoView
from django.http import HttpResponse
from gimnasio.models import *
from gimnasio.utils import exportar_pdf, exportar_excel
from datetime import datetime

# ====== VISTAS PARA EXPORTAR REPORTES ======

class ExportarRegistrovisitantestemporalesPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CERTIFICACIONES INTERNAS A PDF
    Obtiene todas las certificaciones internas y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Registrovisitantestemporales.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID', 'fecha_registro' ]
        
        # Preparar los datos en formato de tuplas
        datos = [
            (visitante.id, visitante.fecha_registro, )
            for visitante in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Registrovisitantestemporales{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE CERTIFICACIONES INTERNAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarRegistrovisitantestemporalesExcel(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Registrovisitantestemporales.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'fecha_registro']
        
        # Preparar los datos en  tuplas
        datos = [
            (visitante.id, visitante.fecha_registro, )
            for visitante in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Registrovisitantestemporales{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE REGISTRO DE VISITANTES TEMPORALES',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )
    