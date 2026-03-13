from django.shortcuts import render
from django.views.generic import View
from django.views import View as DjangoView
from django.http import HttpResponse
from gimnasio.models import *
from gimnasio.utils import exportar_pdf, exportar_excel
from datetime import datetime
from gimnasio.views.registrovisitantestemporales.views import *
from gimnasio.views.turnosdeentrenadores.views import *
from gimnasio.views.certificacionesinternas.views import *
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
            (a.id,a.fecha_asistencia,a.hora_ingreso,a.hora_salida,f"{a.fk_membresia.fk_usuario.nombre_usuario, a.fk_membresia.fk_usuario.apellido_usuario}",a.fk_membresia.fk_usuario.documento)
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
            (a.id,a.fecha_asistencia,a.hora_ingreso,a.hora_salida,f"{a.fk_membresia.fk_usuario.nombre_usuario, a.fk_membresia.fk_usuario.apellido_usuario}",a.fk_membresia.fk_usuario.documento)
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
            (m.id,m.fecha_inicio, m.fecha_fin,f"{m.fk_usuario.nombre_usuario,m.fk_usuario.apellido_usuario}",m.fk_usuario.documento)
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
            (m.id,m.fecha_inicio, m.fecha_fin,f"{m.fk_usuario.nombre_usuario,m.fk_usuario.apellido_usuario}",m.fk_usuario.documento)
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

class ExportarTurnodeentrenadorPDF(DjangoView):
    """
    VISTA PARA EXPORTAR TURNO DE ENTRENADOR A PDF
    Obtiene todos los turnos de entrenador y los exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Turnosentrenadores.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID', 'Administrador', 'fecha_turno_inicio', 'fecha_turno_final', 'Jornada']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (turno.id, turno.administrador.get_full_name() if turno.administrador else "Sin administrador", turno.fecha_turno_inicio, turno.fecha_turno_final, turno.jornada)
            for turno in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Turnodeentrenador {datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE TURNO DE ENTRENADOR ',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )
        
class ExportarTurnodeentrenadorExcel(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Turnosentrenadores.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'Administrador', 'fecha_turno_inicio', 'fecha_turno_final', 'Jornada']
        
        # Preparar los datos en  tuplas
        datos = [
            (turno.id, turno.administrador.get_full_name() if turno.administrador else "Sin administrador", turno.fecha_turno_inicio, turno.fecha_turno_final, turno.jornada)
            for turno in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'Turnodeentrenador{datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE TURNO DE ENTRENADOR',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )


class ExportarCertificacioninternaPDF(DjangoView):
    """
    VISTA PARA EXPORTAR CERTIFICACIONES INTERNAS A PDF
    Obtiene todas las certificaciones internas y las exporta en formato PDF
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Certificacion_interna.objects.all()
        
        # Definir las columnas que se muestran en el reporte
        columnas = ['ID', 'descripcion_certificacion', 'fecha_certificacion', 'fk_Asistencia']
        
        # Preparar los datos en formato de tuplas
        datos = [
            (turno.id, turno.descripcion_certificacion, turno.fecha_certificacion, turno.fk_Asistencia)
            for turno in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'CertificacionesInternas {datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a PDF
        return exportar_pdf(
            titulo='REPORTE DE CERTIFICACIONES INTERNAS',
            columnas=columnas,
            datos=datos,
            nombre_archivo=nombre_archivo
        )
        
class ExportarCertificacioninternaExcel(DjangoView):
    """
    VISTA PARA EXPORTAR CATEGORIAS A EXCEL
    Obtiene todas las categorias y las exporta en formato Excel
    """
    
    def get(self, request):
        # Obtener todas las certificaciones internas
        registro = Certificacion_interna.objects.all()
        
        # Definir las columnas que se mostraran en el reporte
        columnas = ['ID', 'descripcion_certificacion', 'fecha_certificacion', 'fk_Asistencia']
        
        # Preparar los datos en  tuplas
        datos = [
            (turno.id, turno.descripcion_certificacion, turno.fecha_certificacion, turno.fk_Asistencia)
            for turno in registro
        ]
        
        # Generar nombre del archivo con timestamp
        nombre_archivo = f'CertificacionesInternas {datetime.now().strftime("%d_%m_%Y")}'
        
        # Llamar funcion de exportacion a Excel
        return exportar_excel(
            titulo='REPORTE DE CERTIFICACIONES INTERNAS',
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































