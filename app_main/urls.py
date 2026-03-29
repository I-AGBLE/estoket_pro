from django.urls import path

# Views Import From Views Folder
from .views.company_views import company_index, company_dashboard, custom_website
from .views.freelancer_views import freelancer_index, freelancer_dashboard
from .views.links_view import links_index


app_name = "app_main"
urlpatterns = [
    # Freelancer URL
    path("freelancer/", freelancer_index, name="freelancer_index"),
    path("freelancer_dashboard/", freelancer_dashboard, name="freelancer_dashboard"),
    
    #Links URL
    path("links/", links_index, name="links_index"),
    
    # Company URL
    path("company/", company_index, name="company_index"),
    path("company_dashboard/", company_dashboard, name="company_dashboard"),
    path('<slug:slug>/', custom_website, name='custom_website')
]
