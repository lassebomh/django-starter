from typing import Any

from django.contrib.auth import views as auth_views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def root(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/root.html")


class LoginView(auth_views.LoginView):
    template_name = "pages/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    template_name = "pages/logout.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, self.get_context_data())
