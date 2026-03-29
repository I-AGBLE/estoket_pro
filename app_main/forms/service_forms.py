from django import forms
from ..models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_title', 'category', 'service_description', 'service_image']

        widgets = {
            'service_title': forms.TextInput(attrs={
                'placeholder': 'Enter service title',
                'class': 'form-control'
            }),

            # 👇 NEW CATEGORY FIELD
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter or select a category',
                'class': 'form-control',
                'list': 'category-list'  # connects to <datalist>
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
            'category': 'Category',  # 👈 added
            'service_description': 'Service Description',
            'service_image': 'Service Image',
        }