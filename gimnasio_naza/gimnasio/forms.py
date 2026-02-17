from django.forms import ModelForm
from gimnasio.models import Registrovisitantestemporales
from gimnasio.models import Turnosentrenadores
from gimnasio.models import Certificacion_interna

class RegistrovisitantetemporalForm(ModelForm):
    class Meta:
        model = Registrovisitantestemporales
        fields = '__all__'
        
class TurnodeentrenadorForm(ModelForm):
    class Meta:
        model = Turnosentrenadores
        fields = '__all__'
        
class CertificacioninternaForm(ModelForm):
    class Meta:
        model = Certificacion_interna
        fields = '__all__'