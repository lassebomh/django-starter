from typing import Any, Dict

from django.http import HttpRequest

from mysite import settings as SETTINGS


def context_settings(request: HttpRequest) -> Dict[str, Any]:
    return {
        'settings': {
            'DJANGO_VITE_DEV_MODE': SETTINGS.DJANGO_VITE_DEV_MODE
        }
    }