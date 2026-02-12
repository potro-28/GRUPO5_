from django.forms import ModelForm
from gimnasio.models import Registrovisitantestemporales
from gimnasio.models import Turnosentrenadores

class RegistrovisitantetemporalForm(ModelForm):
    class Meta:
        model = Registrovisitantestemporales
        fields = '__all__'
        
class TurnodeentrenadorForm(ModelForm):
    class Meta:
        model = Turnosentrenadores
        fields = '__all__'