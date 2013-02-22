from django.test import TestCase
from django.contrib.auth.models import User
from salad_machine.models import UserFruits, UserSalads
from salad_machine import spec
import random
import pickle

class SaladTest(TestCase):
    fixtures = ["user.json", "salad.json"]
    def setUp(self):
        self.user = User.objects.get(id=1)

    def test_get_random_basket(self):
        level = random.randint(0, len(spec.SPECS)-1)
        basket = UserFruits.objects.get_random_basket(level)
        self.assertTrue(len(basket) <= len(spec.SPECS))

    def test_has_enough_fruits(self):
        fruit = {
            "id" : 0,
            "qty" : 2,
            }
        flag = UserFruits.objects.has_enough_fruits(self.user, fruit)
        self.assertTrue(flag)
        
    def test_has_enough_fruits_fail(self):
        fruit = {
            "id" : 0,
            "qty" : 200,
            }
        flag = UserFruits.objects.has_enough_fruits(self.user, fruit)
        self.assertFalse(flag)

    def test_pick_fruit(self):
        fruit = {
            "id" : 0,
            "qty" : 2,
            }
        rec = UserFruits.objects.get_rec(self.user, fruit)
        self.assertTrue(rec is not None)
        rec_after_pic = UserFruits.objects.pick_fruit(self.user, fruit)
        self.assertTrue(rec_after_pic is not None)
        self.assertEquals(rec.qty, rec_after_pic.qty + fruit.get('qty'))

    def test_pick_fruit_fail(self):
        fruit = {
            "id" : 0,
            "qty" : 200,
            }
        rec = UserFruits.objects.get_rec(self.user, fruit)
        self.assertTrue(rec is not None)
        rec_after_pic = UserFruits.objects.pick_fruit(self.user, fruit)
        self.assertTrue(rec_after_pic is None)
        rec_latest = UserFruits.objects.get_rec(self.user, fruit)
        self.assertEquals(rec.qty, rec_latest.qty)
        

    def test_new_salad(self):
        level = random.randint(0, len(spec.SPECS)-1)
        basket = UserFruits.objects.get_random_basket(level)
        salad = UserSalads.objects.new_salad(self.user, basket)
        self.assertTrue(salad is not None)
        self.assertEquals(salad.fruits, pickle.dumps(basket))

    def test_salad_pick_fruit(self):
        level = random.randint(0, len(spec.SPECS)-1)
        basket = UserFruits.objects.get_random_basket(level)
        salad = UserSalads.objects.new_salad(self.user, basket)
        self.assertTrue(salad.pick_fruits is None)

        fruit = {
            "id" : 0,
            "qty" : 2,
            }

        rec = UserFruits.objects.get_rec(self.user, fruit)
        self.assertTrue(rec is not None)

        salad_after_pick = UserSalads.objects.pick_fruit(salad.id, fruit)
        self.assertTrue(salad_after_pick is not None)
        self.assertTrue(salad_after_pick.pick_fruits is not None)
        pick_fruits = pickle.loads(salad_after_pick.pick_fruits)
        self.assertEqual(pick_fruits.get(fruit.get('id')), fruit.get('qty'))

        rec_after_pic = UserFruits.objects.get_rec(self.user, fruit)
        self.assertTrue(rec_after_pic is not None)
        self.assertEquals(rec.qty, rec_after_pic.qty + fruit.get('qty'))



