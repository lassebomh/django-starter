from django.urls import path

from . import views

urlpatterns = [
    path("", views.root),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
]
