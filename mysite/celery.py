import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = Celery("mysite")

app.config_from_object("mysite.settings", namespace="CELERY")
app.conf.update(dict(result_extended=True))

app.autodiscover_tasks()
