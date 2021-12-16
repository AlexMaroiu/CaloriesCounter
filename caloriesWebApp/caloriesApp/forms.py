from django import forms
from .models import *
from bootstrap_datepicker_plus.widgets import *


class AdaugaArticol(forms.ModelForm):
    class Meta:
        model = Articol
        fields = ['nume', 'firma', 'calorii']

        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control', 'id': 'nume', 'name': 'nume', 'placeholder': 'Nume produs'}),
            'firma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume firma'}),
            'calorii': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calorii'})
        }
