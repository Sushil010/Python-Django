from django import forms
from .models import Aeroplane


class AeroVarietyForm(forms.Form):
    aero_variety=forms.ModelChoiceField(queryset=Aeroplane.objects.all(),empty_label="Select Aeroplane")