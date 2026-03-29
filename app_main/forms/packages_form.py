from django import forms
from ..models import ServicePackage



class ServicePackageForm(forms.ModelForm):
    class Meta:
        model = ServicePackage
        fields = ['package_type', 'package_price', 'package_desc']
        widgets = {
            'package_type': forms.Select(attrs={'class': 'form-control'}),
            'package_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'package_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }