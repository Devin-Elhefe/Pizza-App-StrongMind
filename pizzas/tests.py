from django.test import TestCase
from .models import Topping

class ToppingTests(TestCase):
    def test_create_topping(self):
        topping = Topping.objects.create(name="Cheese")
        self.assertEqual(topping.name, "Cheese")
        self.assertTrue(Topping.objects.filter(name="Cheese").exists())

