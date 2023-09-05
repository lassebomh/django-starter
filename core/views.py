from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/accounts/profile.html")
