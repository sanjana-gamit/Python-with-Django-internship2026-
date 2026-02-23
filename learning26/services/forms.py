from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            'serviceName': forms.TextInput(attrs={'class': 'form-control'}),
            'serviceDescription': forms.Textarea(attrs={'class': 'form-control'}),
            'servicePrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'serviceStatus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }