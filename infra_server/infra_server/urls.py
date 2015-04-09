from django.contrib import admin
from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_api import views

urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/biometrics/populate', views.populate_table),
    #url(r'^api/v1/biometrics/$', views.resource_get),
    url(r'^api/v1/biometrics/$', views.GetAllUser.as_view()),
    url(r'^api/v1/biometrics/(?P<cura_user>\w+)/$', views.GetCuraUser.as_view()),
    url(r'^api/v1/biometrics/(?P<cura_user>\w+)/(?P<start>\d+)/(?P<end>\d+)/$', views.GetTimeUser.as_view()),
)
