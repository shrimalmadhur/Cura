from django.contrib import admin
from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_api import views

userpatterns = patterns('',
    url(r'^api/v1/users/$', views.GetUser.as_view()),
)

biometricspatterns = patterns('',

    url(regex = r'^api/v1/biometrics/populate', 
        view = views.populate_table),

    url(regex = r'^api/v1/biometrics/$', 
        view = views.GetBiometricsData.as_view()),

    url(regex = r'^api/v1/biometrics/(?P<cura_user>\w+)/$', 
        view = views.GetCuraUser.as_view()),

    url(regex = r'^api/v1/biometrics/(?P<cura_user>\w+)/(?P<start>\d+)/(?P<end>\d+)/$', 
        view = views.GetTimeUser.as_view()),
)

restapiurlpatterns = patterns('', 
)

restapiurlpatterns += biometricspatterns
restapiurlpatterns += userpatterns 
