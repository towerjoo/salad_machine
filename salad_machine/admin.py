from django.contrib import admin
from salad_machine.models import UserFruits, UserSalads

class UserFruitsAdmin(admin.ModelAdmin):
    pass

class UserSaladsAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserFruits, UserFruitsAdmin)
admin.site.register(UserSalads, UserSaladsAdmin)
