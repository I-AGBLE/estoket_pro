from django import forms
from ..models import Links

class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['platform', 'address']
        widgets = {
            'platform': forms.Select(attrs={
                'class': 'form-control'
            }),
            'address': forms.URLInput(attrs={
                'placeholder': 'https://example.com/your-profile',
                'class': 'form-control'
            }),
        }

    # Optional: extra validation
    def clean_address(self):
        address = self.cleaned_data.get('address')

        if address and not address.startswith(('http://', 'https://')):
            raise forms.ValidationError(
                "URL must start with http:// or https://"
            )

        return address