from gimnasio.models import Asistencia,Membresia,Mantenimiento
from django.utils import timezone
from datetime import timedelta
def calcular_dias(usuario):
    try:
        membresia = Membresia.objects.filter(fk_usuario = usuario).first()
        if membresia:
            asistencia = Asistencia.objects.filter(fk_membresia = membresia)
            dias = 0
            fecha_inicio = membresia.fecha_inicio
            dia_actual = timezone.now().date()
            print(dia_actual)
            while fecha_inicio <= dia_actual:
                asistio = asistencia.filter(
                    fecha_asistencia = fecha_inicio
                ).exists()
                if not asistio:
                    dias += 1
                
                fecha_inicio += timedelta(days=1)
            
            return dias
        else:
            return None
    except Exception as e:
        print("Error" , e)
        
        
def buscar_mantenimiento():
    mantenimiento = Mantenimiento.objects.order_by(
        "-id"
    ).first()
    return mantenimiento