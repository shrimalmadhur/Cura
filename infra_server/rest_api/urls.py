from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_api import views
#from rest_api import views_contacts

homeautomation_list = views.HomeAutomationViewSet.as_view({
        'get': 'list',
        'put' : 'update',
        'delete' : 'destroy',
}) 

contactspatterns = patterns('',
                            url(r'^api/v1/contacts/(?P<user_name>\w+)/$', views.ContactsByUser.as_view()),
                            url(r'^api/v1/contacts/$', views.ContactsPost.as_view()),)

medicationpatterns = patterns('',
                              url(r'^api/v1/medication/(?P<user_name>\w+)/$', views.MedicationByUser.as_view()),
                              url(r'^api/v1/medication/$', views.MedicationPost.as_view()),)

eventspatterns = patterns('',
    url(r'^api/v1/events/(?P<user_name>\w+)/$', views.EventsByUser.as_view()),
    url(r'^api/v1/events/$', views.EventsPost.as_view()),)

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
    url(r'^api/v1/homeAutomation/$', views.HomeAutomationPostGet.as_view()),
    url(r'^api/v1/homeAutomation/(?P<user_name>\w+)/$', homeautomation_list),
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
restapiurlpatterns += eventspatterns
restapiurlpatterns += medicationpatterns
restapiurlpatterns += contactspatterns
restapiurlpatterns += homeautomationpatterns
restapiurlpatterns += stresspatterns 
