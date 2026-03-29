from django import forms
from ..models import Expertise

class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = ['expertise_title', 'expertise_about']
        widgets = {
            'expertise_title': forms.TextInput(attrs={'class': 'form-control'}),
            'expertise_about': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }