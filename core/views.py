from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {}

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    context["formatted_now"] = formatted_now

    return render(request, "root.html", context)


def counter(request: HttpRequest) -> HttpResponse:
    print(request)
    return render(request, "template.html")
