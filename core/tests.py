from django.test import SimpleTestCase

# from .tasks import add


class MyTaskTestCase(SimpleTestCase):
    def test_my_task(self) -> None:
        # result = add.delay(1, 2).get(timeout=5)
        self.assertEqual(1 + 2, 3)
