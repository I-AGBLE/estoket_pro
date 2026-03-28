from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username")  # added field
    about = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows": 3}), label="About You"
    )
    avatar = forms.ImageField(required=False, label="Profile Image")

    class Meta:
        model = CustomUser
        fields = (
            "username",  # included username
            "first_name",
            "last_name",
            "email",
            "user_type",
            "about",
            "avatar",
            "password1",
            "password2",
        )
        
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "user_type": "User Type",
            "password1": "Password",
            "password2": "Confirm Password",
        }


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
