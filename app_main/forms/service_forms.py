from django import forms
from ..models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_title', 'service_description', 'service_image']
        widgets = {
            'service_title': forms.TextInput(attrs={
                'placeholder': 'Enter service title',
                'class': 'form-control'
            }),
            'service_description': forms.Textarea(attrs={
                'placeholder': 'Describe your service in detail',
                'class': 'form-control',
                'rows': 5
            }),
            'service_image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }

        labels = {
            'service_title': 'Service Title',
            'service_description': 'Service Description',
            'service_image': 'Service Image',
        }
