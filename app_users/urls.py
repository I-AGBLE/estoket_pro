from django.urls import path
from .views import signup_view, login_view


app_name = 'app_users'
urlpatterns = [
    path('', login_view, name='index'),
    path('signup/', signup_view, name='signup'),
]