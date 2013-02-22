from tastypie.resources import ModelResource
from salad_machine.models import UserFruits, UserSalads


class UserFruitsResource(ModelResource):
    class Meta:
        queryset = UserFruits.objects.all()
        resource_name = 'fruit'

class UserSaladsResource(ModelResource):
    class Meta:
        queryset = UserSalads.objects.all()
        resource_name = 'salad'
