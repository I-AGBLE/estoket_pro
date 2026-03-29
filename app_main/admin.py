from django.contrib import admin

from .models import Company, Freelancer, Service, ServicePackage, Links


# Register your models here.
admin.site.register(Company)
admin.site.register(Freelancer)
admin.site.register(Service)
admin.site.register(ServicePackage)
admin.site.register(Links)



