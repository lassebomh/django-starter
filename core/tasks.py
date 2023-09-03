import time

from celery import shared_task


@shared_task()
def add(x: int, y: int) -> int:
    time.sleep(2)
    return x + y

