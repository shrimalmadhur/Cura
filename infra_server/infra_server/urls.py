from django.contrib import admin
from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_api import urls as rest_api_urls

urlpatterns = patterns('', 
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/v1/users/authentication/', include('rest_auth.urls')),
    #url(r'^api/v1/users/registration/', include('rest_auth.registration.urls'))
)

urlpatterns += rest_api_urls.restapiurlpatterns
