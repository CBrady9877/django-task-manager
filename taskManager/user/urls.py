from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.user_view, name="user"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.login_user, name="logout"),
]
