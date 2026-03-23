from django.urls import path
from .views import signup_view, index


app_name = 'app_users'
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
]