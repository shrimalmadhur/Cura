from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_api import views

washroompatterns = patterns('',
    url(r'^api/v1/washroom/(?P<user_name>\w+)/$', views.WashroomGetDestroy.as_view()),
    url(r'^api/v1/washroom/$', views.WashroomPost.as_view()),)

weightpatterns = patterns('',
    url(r'^api/v1/weight/(?P<user_name>\w+)/$', views.WeightGetDestroy.as_view()),
    url(r'^api/v1/weight/$', views.WeightPost.as_view()),)

biometricsprecisepatterns = patterns('',
    url(r'^api/v1/biometricsprecise/(?P<user_name>\w+)/$', views.GetBiometricsPrecise.as_view()),
    url(r'^api/v1/biometricsprecise/$', views.PostBiometricsPrecise.as_view()),
)

notificationpatterns = patterns('',
    url(r'^api/v1/notifications/$', views.notify),
)

userpatterns = patterns('',
    url(r'^api/v1/users/$', views.GetUser.as_view()),
)

biometricspatterns = patterns('',
    url(regex = r'^api/v1/biometrics/$', 
        view = views.GetBiometricsData.as_view()),

    url(regex = r'^api/v1/biometrics/(?P<user_name>\w+)/$', 
        view = views.GetCuraUser.as_view()),

    url(regex = r'^api/v1/biometrics/(?P<user_name>\w+)/(?P<start>\d+)/(?P<end>\d+)/$', 
        view = views.GetTimeUser.as_view()),
)

homeautomationpatterns = patterns('',
    url(r'^api/v1/homeAutomation/$', views.HomeAutomationAPI.as_view()),
    url(r'^api/v1/homeAutomation/(?P<user_name>\w+)/$', views.HomeAutomationUserUpdate.as_view()),
)

stresspatterns = patterns('',
    url(r'^api/v1/stress/$', views.StressView.as_view()),
    url(r'^api/v1/stress/(?P<user_name>\w+)/$', views.StressByUser.as_view()),
)    

restapiurlpatterns = patterns('', 
)

restapiurlpatterns += biometricspatterns
restapiurlpatterns += userpatterns 
restapiurlpatterns += notificationpatterns 
restapiurlpatterns += biometricsprecisepatterns 
restapiurlpatterns += washroompatterns 
restapiurlpatterns += weightpatterns 
restapiurlpatterns += homeautomationpatterns
restapiurlpatterns += stresspatterns 
