from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    about = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows':3}),
        label='About You'
    )
    avatar = forms.ImageField(required=False, label='Profile Image')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'user_type', 'about', 'avatar', 'password1', 'password2')
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'user_type': 'User Type',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }