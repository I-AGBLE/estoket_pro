from django.db import models

PACKAGE_CHOICES = [
    ('basic', 'Basic'),
    ('standard', 'Standard'),
    ('premium', 'Premium'),
]

class ServicePackage(models.Model):
    service = models.ForeignKey(
        'Service', 
        on_delete=models.CASCADE, 
        related_name='packages'
    )
    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_desc = models.TextField()

    class Meta:
        unique_together = ('service', 'package_type')  # prevents duplicate types per service

    def __str__(self):
        return f"{self.service.service_title} - {self.package_type}"