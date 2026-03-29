from django.db import models
from .service import Service

class Expertise(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='expertises')
    expertise_title = models.CharField(max_length=255)
    expertise_about = models.TextField()

    def __str__(self):
        return f"{self.service.service_title} - {self.expertise_title}"