from django import forms
from gimnasio.models import Elemento

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = '__all__'


class usuarioForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = '__all__'
