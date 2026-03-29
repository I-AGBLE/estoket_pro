from django import forms
from ..models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['faq_question', 'faq_answer']
        widgets = {
            'faq_question': forms.TextInput(attrs={'class': 'form-control'}),
            'faq_answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }