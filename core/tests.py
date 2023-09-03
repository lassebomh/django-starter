from django.test import TestCase

from .tasks import add

# Create your tests here.
class YourTestClass(TestCase):
    def test_example(self) -> None:
        self.assertEqual(1 + 1, 2)

    # def test_celery_add(self) -> None:
    #     print("Getting result...")
    #     result = add.delay(3, 2).get()
    #     print("Got result!", result)
    #     self.assertEqual(result, 5)
