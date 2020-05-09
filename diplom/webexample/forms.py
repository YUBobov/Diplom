from django import forms

from .models import FTTx


class FTTxForm(forms.ModelForm):



    class Meta:
        model = FTTx
        fields = (
            'name',
            'volokno',
            'kN',
            'price',
            'link',
        )
        widgets = {
            'name': forms.TextInput,
            'kN': forms.TextInput
        }