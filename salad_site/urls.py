from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from salad_machine.api import UserFruitsResource, UserSaladsResource
from tastypie.api import Api
v1_api = Api(api_name='v1')
v1_api.register(UserFruitsResource())
v1_api.register(UserSaladsResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salad_machine.views.home', name='home'),
    # url(r'^salad_machine/', include('salad_machine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
