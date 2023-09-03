from django.db.models import QuerySet
from django_celery_results.models import TaskResult
from django_unicorn.components import PollUpdate, UnicornView

from ..tasks import add


class MycomponentView(UnicornView):
    tasks: QuerySet[TaskResult] = TaskResult.objects.none()
    has_started = False
    a = 1
    b = 1

    def update_tasks(self) -> PollUpdate:
        self.tasks = TaskResult.objects.filter(task_name=add.name).order_by('-date_created')
        self.has_started = self.tasks.filter(status='STARTED').count() > 0

        return PollUpdate(timing=200 if self.has_started else 10000, method="update_tasks")

    def mount(self) -> None:
        self.update_tasks()

    def new_task(self) -> PollUpdate:
        add.delay(int(self.a), int(self.b))
        self.update_tasks()
        self.has_started = True

        return PollUpdate(timing=200, method="update_tasks")
