from django.forms import ModelForm
from gimnasio.models import Masa_corporal
from django.forms import ModelForm
from gimnasio.models import Sancion

class Masa_muscularForm(ModelForm):
    class Meta:
        model = Masa_corporal
        fields = '__all__'

class SancionesForm(ModelForm):
    class Meta:
        model = Sancion
        fields = '__all__'
