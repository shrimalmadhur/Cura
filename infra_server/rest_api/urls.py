from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_api import views

fmt = '\d{4}-\d{2}-\d{2}'

homeautomation_list = views.HomeAutomationViewSet.as_view({
        'get': 'list',
        'put' : 'update',
}) 

washroom_list = views.WashroomCount.as_view({
        'get': 'list',
}) 

biometrics_post_list = views.BiometricsPost.as_view({
    'post' : 'create',
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

stress_list = views.StressGetTime.as_view({
    'get' : 'list',
})

weight_list = views.WeightGetTime.as_view({
    'get' : 'list',
})

blood_oxygen_list = views.BloodOxygenGetTime.as_view({
    'get' : 'list',
})

blood_pressure_list = views.BloodPressureGetTime.as_view({
    'get' : 'list',
})

blood_pressure_post_list = views.BloodPressurePost.as_view({
    'post' : 'create',
})

stress_recent_list = views.StressRecent.as_view({
    'get' : 'list',
})

biometrics_list = views.BiometricsGetTime.as_view({
    'get' : 'list',
})

heart_rate_list = views.HeartRate.as_view({
    'get' : 'list',
})

breathing_rate_list = views.BreathingRate.as_view({
    'get' : 'list',
})

posture_list = views.Posture.as_view({
    'get' : 'list',
})

skin_temperature_list = views.SkinTemperature.as_view({
    'get' : 'list',
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


washroompatterns = patterns('',
    url(r'^api/v1/washroom/(?P<user_name>\w+)/$', views.WashroomGetDestroy.as_view()),
    url(r'^api/v1/washroom/$', views.WashroomPost.as_view()),
    url(r'^api/v1/washroom/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), washroom_list),) 

weightpatterns = patterns('',
    url(r'^api/v1/weight/(?P<user_name>\w+)/$', views.GetWeight.as_view()),
    url(r'^api/v1/weight/$', views.PostWeight.as_view()),
    url(r'^api/v1/weight/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), weight_list), 
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
        view = biometrics_post_list),

    url(regex = r'^api/v1/biometrics/(?P<user_name>\w+)/$', 
        view = views.GetCuraUser.as_view()),

    url(regex = r'^api/v1/biometrics/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), view = biometrics_list),
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
    #url(r'^api/v1/stress/recent/(?P<user_name>\w+)/$', stress_recent_list),
    url(r'^api/v1/stress/recent/(?P<user_name>\w+)/$', views.get_stress_recent),
    url(r'^api/v1/stress/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), stress_list), 
)

bloodoxygenpatterns = patterns('',
                               url(r'^api/v1/bloodoxygen/$', views.BloodOxygenView.as_view()),
                               url(r'^api/v1/bloodoxygen/(?P<user_name>\w+)/$', views.BloodOxygenByUser.as_view()),
                               url(r'^api/v1/bloodoxygen/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), blood_oxygen_list), 
)

bloodpressurepatterns = patterns('',
                                 url(r'^api/v1/bloodpressure/$', blood_pressure_post_list),
                                 url(r'^api/v1/bloodpressure/(?P<user_name>\w+)/$', views.BloodPressureByUser.as_view()),
                                 url(r'^api/v1/bloodpressure/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), blood_pressure_list),) 

graphpatterns = patterns('',
    url(regex = r'^api/v1/iexpress/heartrate/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = heart_rate_list ),

    url(regex = r'^api/v1/iexpress/breathingrate/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = breathing_rate_list ),

    url(regex = r'^api/v1/iexpress/posture/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = posture_list ),
    
    url(regex = r'^api/v1/iexpress/skintemperature/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), view = skin_temperature_list ),
)

restapiurlpatterns = patterns('', 
)

restapiurlpatterns += biometricspatterns
restapiurlpatterns += userpatterns 
restapiurlpatterns += notificationpatterns 
#restapiurlpatterns += alertspatterns 
restapiurlpatterns += biometricsprecisepatterns 
restapiurlpatterns += washroompatterns 
restapiurlpatterns += weightpatterns
restapiurlpatterns += eventspatterns
restapiurlpatterns += medicationpatterns
restapiurlpatterns += contactspatterns
restapiurlpatterns += homeautomationpatterns
restapiurlpatterns += moodlightpatterns
restapiurlpatterns += stresspatterns
restapiurlpatterns += bloodoxygenpatterns
restapiurlpatterns += bloodpressurepatterns
restapiurlpatterns += graphpatterns 
