from django.urls import path
from .views import freelancer_index, company_index


app_name = 'app_main'
urlpatterns = [
    path('freelancer/', freelancer_index, name='freelancer_index'),
    path('company/', company_index, name='company_index'),
]