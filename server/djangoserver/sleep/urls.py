from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'sessions', SessionViewSet)

urlpatterns = patterns('',
  url(r'^', include(router.urls)),
)

