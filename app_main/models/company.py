from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid
import os

User = get_user_model()

# 👇 Custom function for unique image names
def company_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]  # get file extension
    unique_filename = f"{uuid.uuid4()}.{ext}"  # generate unique name
    return os.path.join('company_images/', unique_filename)


class Company(models.Model):
    COMPANY_SIZE_CHOICES = [
        ('1-20', '1-20'),
        ('20-50', '20-50'),
        ('50-100', '50-100'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    company_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    company_about = RichTextField(config_name='default')
    company_location = models.CharField(max_length=255)
    company_year_founded = models.DateField()
    company_industry = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_size = models.CharField(max_length=10, choices=COMPANY_SIZE_CHOICES)

    # ✅ Updated image field
    company_image = models.ImageField(
        upload_to=company_image_upload_path,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.company_name)
            slug = base_slug
            counter = 1

            while Company.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name