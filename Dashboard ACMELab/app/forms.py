from django import forms
from app.models import SC2

class Amostramodelform(forms.ModelForm):
    class Meta:
        model = SC2
        fields = '__all__'

class FilterForm(forms.Form):
    laboratorio_name = forms.ChoiceField(
        choices=[],
        required=False,
        label='Laboratório'
    )
    
    melhor_repeticao_name = forms.ChoiceField(
        choices=[],
        required=False,
        label='Repetição'
    )
    
    lote_number = forms.ChoiceField(
        choices=[],
        required=False,
        label='Lote'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Obtendo nomes únicos de laboratórios, repetições e números de lote
        laboratorios = SC2.objects.values_list('laboratorio__name', flat=True).distinct()
        repeticoes = SC2.objects.values_list('melhor_repeticao__name', flat=True).distinct()
        lotes = SC2.objects.values_list('lote', flat=True).distinct()

        # Atualizando as opções de escolha para os campos
        self.fields['laboratorio_name'].choices = [('', 'Todos')] + [(lab, lab) for lab in laboratorios]
        self.fields['melhor_repeticao_name'].choices = [('', 'Todos')] + [(rep, rep) for rep in repeticoes]
        self.fields['lote_number'].choices = [('', 'Todos')] + [(lote, str(lote)) for lote in lotes]

