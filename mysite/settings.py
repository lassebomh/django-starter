"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from django.urls import reverse_lazy

from core.monkeypatch import monkeypatch

getenv = os.environ.get


BASE_DIR = Path(__file__).resolve().parent.parent

MODE = getenv("MODE")

if MODE == "development":
    monkeypatch()

DEBUG = MODE != "production"

SECRET_KEY = getenv("DJANGO_SECRET_KEY", "django-insecure-1234567890")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # Builtin
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # First party
    "core",
    "core.templatetags",
    "search",
    "public_site",
    # Third party
    "django_vite",
    "django_unicorn",
    "django_celery_results",
    "django_celery_beat",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

if MODE == "staging":
    MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]


LOGIN_REDIRECT_URL = reverse_lazy("account_profile")
LOGIN_URL = reverse_lazy("login")
LOGOUT_REDIRECT_URL = reverse_lazy("root")

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.context_settings",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"


WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_USER"),
        "PASSWORD": getenv("POSTGRES_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST"),
        "POST": getenv("POSTGRES_PORT"),
        # 'OPTIONS': {'sslmode': 'require'},
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{getenv('REDIS_PROTOCOL')}://{getenv('REDIS_USER')}:{getenv('REDIS_PASSWORD')}@{getenv('REDIS_HOST')}:{getenv('REDIS_PORT')}",
    }
}

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BROKER_URL = CACHES["default"]["LOCATION"]

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = DEBUG

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    # Definition of filters
    "filters": {"hide_staticfiles": {"()": "mysite.logger.SkipStaticFilter"}},
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler", "filters": ["hide_staticfiles"]},
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    },
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

INTERNAL_IPS = [
    "127.0.0.1",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_URL = "/static/"

# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = getenv("STATIC_DIST_DIR")

# If use HMR or not.
DJANGO_VITE_DEV_MODE = MODE == "development"

# Name of static files folder (after called python manage.py collectstatic)
STATIC_ROOT = BASE_DIR / "collectstatic"

# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS = [
    DJANGO_VITE_ASSETS_PATH,
    BASE_DIR / "static",
]

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "mysite"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"
