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

class ExportarmantenimientoPDF(DjangoView):
    """
    VISTA PARA EXPORTAR MANTENIMIENTO A PDF
    Obtiene todos los mantenimientos y los exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todos los mantenimientos
        mantenimientos = Mantenimiento.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Elemento_id', 'Tipo de mantenimiento', 'Fecha programada', 'Estado']
        
        # Preparar los datos en  tuplas
        datos = [
            (m.id, m.elemento_id, m.tipo_mantenimiento, m.fecha_programada, m.estado)
            for m in mantenimientos
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Mantenimiento_{datetime.now().strftime("%d_%m_%Y")}'

        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE MANTENIMIENTO',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )



class ExportarMantenimientoExcel(DjangoView):
    """
    VISTA PARA EXPORTAR MANTENIMIENTO A EXCEL
    Obtiene todos los mantenimientos y los exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todos los mantenimientos
        mantenimientos = Mantenimiento.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Elemento_id', 'Tipo de mantenimiento', 'Fecha programada', 'Estado']
        
        # Preparar los datos en  tuplas
        datos = [
            (m.id, m.elemento_id, m.tipo_mantenimiento, m.fecha_programada, m.estado)
            for m in mantenimientos
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Reporte_Mantenimiento_{datetime.now().strftime("%d_%m_%Y")}'

        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE MANTENIMIENTO',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )