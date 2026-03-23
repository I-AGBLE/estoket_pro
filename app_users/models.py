from django.db import models
from django.contrib.auth.models import AbstractUser


# ------------------------------------- Custom User Model For Authentication --------------------------------------
USER_TYPE_CHOICES = [
    ('freelancer', 'Freelancer'),
    ('company', 'Company'),
    ('individual', 'Individual'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=11, choices=USER_TYPE_CHOICES, default='individual')
    about = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    full_name.short_description = "Full Name"





