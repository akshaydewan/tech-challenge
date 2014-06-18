from django.conf.urls import patterns, url

from admissions import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^generate/', views.generateData),
    url(r'^rest/admissionrequests/', views.handleRestRequest),
)
