from django.db import models
from django.contrib.auth.models import User
from salad_machine import spec

class UserFruitsManager(models.Manager):
    def get_random_basket(self, level):
        return spec.get_random_basket(level)
        
        

class UserFruits(models.Model):
    user = models.ForeignKey(User, related_name="fruit_user")
    fruit_id = models.IntegerField()
    qty = models.IntegerField()

    objects = UserFruitsManager()

    def __unicode__(self):
        return "%s has %s units fruit" % (self.user.username, self.qty, get_fruit_info_from_id(self.fruit_id).get("name"))

class UserSalads(models.Model):
    user = models.ForeignKey(User, related_name="salad_user")
    name = models.CharField(max_length=100, null=True, blank=True)
    fruits = models.TextField() #a pickled data

    def __unicode__(self):
        return "%s has a salad named %s" % (self.user.username, self.name if self.name else "N/A")
