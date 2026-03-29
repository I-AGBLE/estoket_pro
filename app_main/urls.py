from django.urls import path

from app_main import views

# Views Import From Views Folder
from .views.company_views import company_index, company_dashboard, custom_website
from .views.freelancer_views import freelancer_index, freelancer_dashboard
from .views.links_view import links_index
from .views.service_views import service_index, service_detail
from .views.service_packages import service_packages
from .views.expertise_view import service_expertise
from .views.faqs_view import service_faqs




app_name = "app_main"
urlpatterns = [
    # Freelancer URLs
    path("freelancer/", freelancer_index, name="freelancer_index"),
    path("freelancer_dashboard/", freelancer_dashboard, name="freelancer_dashboard"),
    
    #Links URLs
    path("links/", links_index, name="links_index"),
    
    # Company URLs
    path("company/", company_index, name="company_index"),
    path("company_dashboard/", company_dashboard, name="company_dashboard"),
    
    # Service URLs
    path("service/", service_index, name="service_index"),
    path('service/<int:service_id>/', service_detail, name='service_detail'),
    path('service/<int:service_id>/packages/', service_packages, name='service_packages'),
    path('service/<int:service_id>/expertise/', service_expertise, name='service_expertise'), 
    path('service/<int:service_id>/faqs/', service_faqs, name='service_faqs'),


    
]

# Public URLs
urlpatterns += [
    path('<slug:slug>/', custom_website, name='custom_website'),  
]
