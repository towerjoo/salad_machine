from django.test import TestCase
from salad_machine.models import UserFruits, UserSalads
from salad_machine import spec
import random

class SaladTest(TestCase):
    def test_get_random_basket(self):
        level = random.randint(0, len(spec.SPECS)-1)
        basket = UserFruits.objects.get_random_basket(level)
        self.assertTrue(len(basket) <= len(spec.SPECS))

