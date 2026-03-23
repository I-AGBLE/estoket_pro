from django.contrib import admin
from .models import CustomUser

# CustomUser for user registration
admin.site.register(CustomUser)
