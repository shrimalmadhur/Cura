from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_api import views

homeautomation_list = views.HomeAutomationViewSet.as_view({
        'get': 'list',
        'put' : 'update',
}) 

moodlight_list = views.MoodLightViewSet.as_view({
        'get': 'list',
        'put': 'update',
})

contacts_list = views.ContactsViewSet.as_view({
        'get': 'list',
        'put' : 'update',
}) 

medication_list = views.MedicationViewSet.as_view({
        'get': 'list',
        'put' : 'update',
}) 

events_list = views.EventsViewSet.as_view({
        'get': 'list',
        'put' : 'update',
}) 

contactspatterns = patterns('',
        url(r'^api/v1/contacts/$', views.ContactsPost.as_view()),
        url(r'api/v1/contacts/(?P<user_name>\w+)/$', contacts_list),
        url(r'api/v1/contacts/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_contact),)

medicationpatterns = patterns('',
    url(r'^api/v1/medication/$', views.MedicationPostGet.as_view()),
    url(r'^api/v1/medication/(?P<user_name>\w+)/$', medication_list),
    url(r'api/v1/medication/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_medications),) 
    
eventspatterns = patterns('',
    url(r'^api/v1/events/$', views.EventsPostGet.as_view()),
    url(r'^api/v1/events/(?P<user_name>\w+)/$', events_list),
    url(r'api/v1/events/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_event),) 


'''
washroompatterns = patterns('',
    url(r'^api/v1/washroom/(?P<user_name>\w+)/$', views.WashroomGetDestroy.as_view()),
    url(r'^api/v1/washroom/$', views.WashroomPost.as_view()),)
'''
weightpatterns = patterns('',
    url(r'^api/v1/weight/(?P<user_name>\w+)/$', views.GetWeight.as_view()),
    url(r'^api/v1/weight/$', views.PostWeight.as_view()),
)

biometricsprecisepatterns = patterns('',
    url(r'^api/v1/biometricsprecise/(?P<user_name>\w+)/$', views.GetBiometricsPrecise.as_view()),
    url(r'^api/v1/biometricsprecise/$', views.PostBiometricsPrecise.as_view()),
)

notificationpatterns = patterns('',
    url(r'^api/v1/notifications/$', views.notify),
)

'''
alertspatterns = patterns('',
    url(r'^api/v1/alerts/$', views.alerts),
)
'''

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
    url(r'^api/v1/homeautomation/$', views.HomeAutomationPostGet.as_view()),
    url(r'^api/v1/homeautomation/(?P<user_name>\w+)/$', homeautomation_list),
    url(r'^api/v1/homeautomation/(?P<user_name>\w+)/(?P<tag_id>\w+)/$', views.homeautomation_destroy),
)

moodlightpatterns = patterns('',
    url(r'^api/v1/moodlight/$', views.MoodLightPostGet.as_view()),
    url(r'^api/v1/moodlight/(?P<user_name>\w+)/$', moodlight_list),
    url(r'^api/v1/moodlight/(?P<user_name>\w+)/(?P<device_id>\w+)/$', views.destroy_moodlight),
)

stresspatterns = patterns('',
    url(r'^api/v1/stress/$', views.StressView.as_view()),
    url(r'^api/v1/stress/(?P<user_name>\w+)/$', views.StressByUser.as_view()),
)

bloodoxygenpatterns = patterns('',
                               url(r'^api/v1/bloodoxygen/$', views.BloodOxygenView.as_view()),
                               url(r'^api/v1/bloodoxygen/(?P<user_name>\w+)/$', views.BloodOxygenByUser.as_view()),
                               
                               )
bloodpressurepatterns = patterns('',
                                 url(r'^api/v1/bloodpressure/$', views.BloodPressureView.as_view()),
                                 url(r'^api/v1/bloodpressure/(?P<user_name>\w+)/$', views.BloodPressureByUser.as_view()),
                                 )
restapiurlpatterns = patterns('', 
)

restapiurlpatterns += biometricspatterns
restapiurlpatterns += userpatterns 
restapiurlpatterns += notificationpatterns 
#restapiurlpatterns += alertspatterns 
restapiurlpatterns += biometricsprecisepatterns 
#restapiurlpatterns += washroompatterns 
restapiurlpatterns += weightpatterns
restapiurlpatterns += eventspatterns
restapiurlpatterns += medicationpatterns
restapiurlpatterns += contactspatterns
restapiurlpatterns += homeautomationpatterns
restapiurlpatterns += moodlightpatterns
restapiurlpatterns += stresspatterns
restapiurlpatterns += bloodoxygenpatterns
restapiurlpatterns += bloodpressurepatterns
