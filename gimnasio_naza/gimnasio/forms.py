from django.forms import ModelForm
from gimnasio.models import Masa_corporal

class Masa_muscularForm(ModelForm):
    class Meta:
        model = Masa_corporal
        fields = '__all__'
        