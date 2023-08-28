from django.shortcuts import render
from datetime import datetime
import os

# Create your views here.
def index(request):
    context = {}

    now = datetime.now()

    formatted_now = now.strftime('%A, %d %B, %Y at %X')

    context['formatted_now'] = formatted_now

    return render(request, 'root.html', context)