from django import forms
from usuario.models import Sorteio

class DezenaForm(forms.Form):
    dezenas = forms.CharField(label='Dezenas (Separadas por vírgula)', widget=forms.Textarea)

class SorteioForm(forms.ModelForm):
    quantidade_premios = forms.IntegerField(label='Quantidade de Prêmios', min_value=1)


    class Meta:
        model = Sorteio
        fields = ['numeroEdicao', 'anoEdicao', 'dataEdicao', 'quantidade_premios']