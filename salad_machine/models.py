from django.db import models
from django.contrib.auth.models import User
from salad_machine import spec
import pickle

class UserFruitsManager(models.Manager):
    def get_random_basket(self, level):
        return spec.get_random_basket(level)

    def pick_fruit(self, user, fruit):
        if not self.has_enough_fruits(user, fruit):
            return None
        try:
            rec = self.get(user=user, fruit_id=fruit.get("id"))
            rec.qty = rec.qty - fruit.get("qty")
            rec.save()
            return rec
        except:
            return None
        

    def has_enough_fruits(self, user, fruit):
        try:
            rec = self.get(user=user, fruit_id=fruit.get("id"))
            return rec.qty >= fruit.get("qty")
        except:
            return False
        
    def get_rec(self, user, fruit):
        try:
            rec = self.get(user=user, fruit_id=fruit.get("id"))
            return rec
        except:
            return None

class UserFruits(models.Model):
    user = models.ForeignKey(User, related_name="fruit_user")
    fruit_id = models.IntegerField()
    qty = models.IntegerField()

    objects = UserFruitsManager()

    def __unicode__(self):
        return "%s has %s units fruit named %s" % (self.user.username, self.qty, spec.get_fruit_info_from_id(self.fruit_id).get("name"))

class UserSaladsManager(models.Manager):
    def new_salad(self, user, basket):
        fruits = pickle.dumps(basket)
        salad = self.model(user=user, fruits=fruits)
        salad.save()
        return salad

    def pick_fruit(self, sid, fruit):
        try:
            fid = fruit.get("id")
            salad = self.get(id=sid)
            # check
            if UserFruits.objects.has_enough_fruits(salad.user, fruit):
                # user's fruit will be cost
                UserFruits.objects.pick_fruit(salad.user, fruit)
                pick_fruits = salad.pick_fruits
                if pick_fruits:
                    pick_fruits = pickle.loads(pick_fruits)
                else:
                    pick_fruits = {}
                pick_fruits.update({
                    fruit.get("id"): pick_fruits.get("qty", 0) + fruit.get("qty"),
                    })
                salad.pick_fruits = pickle.dumps(pick_fruits)
                salad.save()
                return salad
            else:
                return None
        except:
            # handle exceptions
            return None

class UserSalads(models.Model):
    user = models.ForeignKey(User, related_name="salad_user")
    name = models.CharField(max_length=100, null=True, blank=True)
    pick_fruits = models.TextField(null=True, blank=True)
    fruits = models.TextField() #a pickled data
    is_done = models.BooleanField(default=False)

    objects = UserSaladsManager()

    def __unicode__(self):
        return "%s has a salad named %s" % (self.user.username, self.name if self.name else "N/A")
