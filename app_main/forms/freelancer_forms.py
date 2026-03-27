from django import forms
from ..models import Freelancer
import re


class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = [
            "freelancer_about",
            "freelancer_location",
            "freelancer_industry",
            "freelancer_phone",
        ]
        widgets = {
            "freelancer_about": forms.Textarea(attrs={"rows": 4}),
        }

    # Validate phone number: digits and optional + only
    def clean_company_phone(self):
        phone = self.cleaned_data.get("company_phone", "").strip()
        if not re.fullmatch(r"\+?\d+", phone):
            raise forms.ValidationError(
                "Phone number must contain only digits and an optional leading +."
            )
        # Remove spaces, dashes, or other characters before saving
        phone = re.sub(r"[^+\d]", "", phone)
        return phone


