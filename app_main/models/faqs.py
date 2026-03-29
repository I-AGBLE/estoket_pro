from django.db import models
from .service import Service

class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    faq_question = models.CharField(max_length=255)
    faq_answer = models.TextField()

    def __str__(self):
        return f"{self.service.service_title} - {self.faq_question}"