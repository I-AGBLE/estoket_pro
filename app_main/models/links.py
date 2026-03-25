from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Links(models.Model):
    PLATFORM_CHOICES = [
        ("website", "Website"),
        ("linkedin", "LinkedIn"),
        ("x", "X"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("github", "Github"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    address = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.platform}"
