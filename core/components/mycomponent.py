from django_celery_results.models import TaskResult
from django_unicorn.components import UnicornView

from ..tasks import add


class MycomponentView(UnicornView):
    tasks = TaskResult.objects.none()

    def mount(self) -> None:
        self.tasks = TaskResult.objects.all()

    def add(self) -> None:
        # add.apply_async((1, 1), ignore_result=True)
        self.tasks = []
