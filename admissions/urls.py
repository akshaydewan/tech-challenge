from django.conf.urls import patterns, url

from admissions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
