from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



# ------------------------------------- Custom User Model For Authentication --------------------------------------
USER_TYPE_CHOICES = [
    ('freelancer', 'Freelancer'),
    ('company', 'Company'),
    ('individual', 'Individual'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=11, choices=USER_TYPE_CHOICES, default='individual')
    about = RichTextField(config_name='default')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

