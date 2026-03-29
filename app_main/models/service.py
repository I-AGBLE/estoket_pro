from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

import os
import uuid
from django.utils.deconstruct import deconstructible


User = get_user_model()




def service_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]  # get file extension
    # generate a unique filename using uuid
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    # optionally, organize by service id or user
    return os.path.join('service_images', unique_filename)



class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    service_title = models.CharField(max_length=255)
    service_description = RichTextField(config_name='default')
    service_image = models.ImageField(
        upload_to=service_image_upload_to,  # use the custom function
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.service_title