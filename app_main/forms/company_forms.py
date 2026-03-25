from django import forms
from ..models import Company
from django.utils import timezone
import re


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "company_name",
            "company_about",
            "company_location",
            "company_year_founded",
            "company_industry",
            "company_email",
            "company_phone",
            "company_size",
            "company_image",
        ]
        widgets = {
            "company_about": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Brief about the company"}
            ),
            "company_year_founded": forms.DateInput(
                attrs={
                    "type": "date",
                    "max": timezone.now().date(),  # HTML5: prevent future dates
                    "placeholder": "YYYY-MM-DD",
                }
            ),
            "company_size": forms.Select(),
            "company_phone": forms.TextInput(
                attrs={
                    "placeholder": "+233501234567",
                    "pattern": r"\+?\d+",
                    "title": "Only numbers allowed, optionally starting with +",
                }
            ),
            "company_image": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",  # only allow images
                    "class": "form-control",  # optional styling (Bootstrap etc.)
                }
            ),
        }

    # Validate company_year_founded is not in the future
    def clean_company_year_founded(self):
        year_founded = self.cleaned_data.get("company_year_founded")
        if year_founded and year_founded > timezone.now().date():
            raise forms.ValidationError("The foundation date cannot be in the future.")
        return year_founded

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
