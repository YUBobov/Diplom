from django import forms

from .models import FTTx
from .models import ADSS


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


class ADSSForm(forms.ModelForm):
    class Meta:
        model = ADSS
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