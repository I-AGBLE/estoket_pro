from django.urls import path
from .views import signup_view, login_view, delete_account


app_name = "app_users"
urlpatterns = [
    path("", login_view, name="index"),
    path("signup/", signup_view, name="signup"),
    
    # app_main/urls.py
    path("delete_account/", delete_account, name="delete_account"),
]
