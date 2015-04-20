from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/auth/', include('cura.urls')),
    url(r'^api/v1/sleep/', include('sleep.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
