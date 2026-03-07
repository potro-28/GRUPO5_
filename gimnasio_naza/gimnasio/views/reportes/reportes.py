from django.shortcuts import render
from django.views.generic import View
from django.views import View as DjangoView
from django.http import HttpResponse
from gimnasio.models import *
from gimnasio.utils import exportar_pdf, exportar_excel
from datetime import datetime

# ====== VISTAS PARA EXPORTAR REPORTES ======

class ExportarElementosPDF(DjangoView):
    """
    VISTA PARA EXPORTAR ELEMENTOS A PDF
    Obtiene todos los elementos y los exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        elemento= Elemento.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Nombre','marca','categoria']
        
        # Preparar los datos en  tuplas
        datos = [
            (e.id, e.nombre_elemento,e.marca,e.categoria_id)
            for e in elemento
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Elementos_{datetime.now().strftime("%d_%m_%Y")}'

        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE ELEMENTOS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarElementosExcel(DjangoView):
    """
    VISTA PARA EXPORTAR ELEMENTOS A EXCEL
    Obtiene todos los elementos y los exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las categorias 
        elemento= Elemento.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Nombre', 'Marca', 'Categoria']
        
        # Preparar los datos en  tuplas
        datos = [
            (e.id, e.nombre_elemento, e.marca, e.categoria_id)
            for e in elemento
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Elementos_{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE ELEMENTOS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )
class ExportarUsuariosPDF(DjangoView):
    """
    VISTA PARA EXPORTAR USUARIOS A PDF
    Obtiene todos los usuarios y los exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todos los usuarios
        usuarios = Usuario.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'documento','genero','nombre ','apellido','correo de','telefono','fecha de nacimiento','estado']
        
        # Preparar los datos en  tuplas
        datos = [
            (u.id, u.documento, u.genero_usuario, u.nombre_usuario, u.apellido_usuario, u.correo_usuario, u.telefono_usuario, u.fecha_nacimiento, u.estado)
            for u in usuarios
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Usuarios_{datetime.now().strftime("%d_%m_%Y")}'

        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE USUARIOS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarUsuariosExcel(DjangoView):
    """
    VISTA PARA EXPORTAR USUARIOS A EXCEL
    Obtiene todos los usuarios y los exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todos los usuarios
        usuarios = Usuario.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'documento','genero del usuario','nombre del usuario','apellido del usuario','correo del usuario','telefono del usuario','fecha de nacimiento del usuario','estado del usuario']
        
        # Preparar los datos en  tuplas
        datos = [
            (u.id, u.documento, u.genero_usuario, u.nombre_usuario, u.apellido_usuario, u.correo_usuario, u.telefono_usuario, u.fecha_nacimiento, u.estado)
            for u in usuarios
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Usuarios_{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE USUARIOS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )
