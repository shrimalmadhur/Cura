from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/sleep/', include('sleep.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
