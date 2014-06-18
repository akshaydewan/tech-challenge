from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from admissions.api.resources import StudentResource, AdmissionRequestResource, AdmissionsByDate

v1_api = Api(api_name='v1')
v1_api.register(StudentResource())
v1_api.register(AdmissionRequestResource())
v1_api.register(AdmissionsByDate())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mpaani.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admissions/', include('admissions.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
