from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'sessions', SessionViewSet)

fmt = '(\d{4}-\d{2}-\d{2})'

urlgraphs = patterns('',
  url(r'^(?P<dtype>\w+)/(?P<uid>\d+)/(?P<begin>%s)/(?P<end>%s)/$' % (fmt, fmt), RangeGraph.as_view()),
  url(r'^(?P<dtype>\w+)/(?P<uid>\d+)/(?P<date>%s)/$' % fmt, DayGraph.as_view()),
)

urlpatterns = patterns('',
  #url(r'^', include(router.urls)),
  url(r'^', include(urlgraphs)),
)

