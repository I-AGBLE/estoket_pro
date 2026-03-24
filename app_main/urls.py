from django.urls import path

# Views Import From Views Folder
from .views.company_views import company_index
from .views.freelancer_views import freelancer_index


app_name = "app_main"
urlpatterns = [
    path("freelancer/", freelancer_index, name="freelancer_index"),
    path("company/", company_index, name="company_index"),
]
