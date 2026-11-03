import platform

import django
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from .models import Visit


def home(request):
    Visit.objects.create()
    return render(request, "core/home.html", {
        "visits": Visit.objects.count(),
        "django": django.get_version(),
        "python": platform.python_version(),
        "database": connection.vendor,
    })


def health(request):
    """The health check: answers without touching the database."""
    return HttpResponse("ok", content_type="text/plain")
