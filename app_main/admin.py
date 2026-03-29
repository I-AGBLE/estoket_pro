from django.contrib import admin
from .models import Company, Freelancer, Service


# Register your models here.
admin.site.register(Company)
admin.site.register(Freelancer)
admin.site.register(Service)

