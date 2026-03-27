from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


User = get_user_model()



class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='freelancer')
    freelancer_about = RichTextField(config_name='default')
    freelancer_location = models.CharField(max_length=255)
    freelancer_industry = models.CharField(max_length=255)
    freelancer_phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

