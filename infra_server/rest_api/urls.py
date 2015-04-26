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
        url(r'^contacts/$', views.ContactsPost.as_view()),
        url(r'^contacts/(?P<user_name>\w+)/$', contacts_list),
        url(r'^contacts/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_contact),)

medicationpatterns = patterns('',
    url(r'^medication/$', views.MedicationPostGet.as_view()),
    url(r'^medication/(?P<user_name>\w+)/$', medication_list),
    url(r'^medication/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_medications),) 
    
eventspatterns = patterns('',
    url(r'^events/$', views.EventsPostGet.as_view()),
    url(r'^events/(?P<user_name>\w+)/$', events_list),
    url(r'events/(?P<user_name>\w+)/(?P<pk>\d+)/$', views.destroy_event),) 


washroompatterns = patterns('',
    url(r'^washroom/(?P<user_name>\w+)/$', views.WashroomGetDestroy.as_view()),
    url(r'^washroom/$', views.WashroomPost.as_view()),
    url(r'^washroom/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), washroom_list),) 

weightpatterns = patterns('',
    url(r'^weight/(?P<user_name>\w+)/$', views.GetWeight.as_view()),
    url(r'^weight/$', views.PostWeight.as_view()),
    url(r'^weight/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), weight_list), 
)

biometricsprecisepatterns = patterns('',
    url(r'^biometricsprecise/(?P<user_name>\w+)/$', views.GetBiometricsPrecise.as_view()),
    url(r'^biometricsprecise/$', views.PostBiometricsPrecise.as_view()),
)

notificationpatterns = patterns('',
    url(r'^notifications/$', views.notify),
)

'''
alertspatterns = patterns('',
    url(r'^alerts/$', views.alerts),
)
'''

userpatterns = patterns('',
    url(r'^users/$', views.GetUser.as_view()),
)

biometricspatterns = patterns('',
    url(regex = r'^biometrics/$', 
        view = biometrics_post_list),

    url(regex = r'^biometrics/(?P<user_name>\w+)/$', 
        view = views.GetCuraUser.as_view()),

    url(regex = r'^biometrics/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), view = biometrics_list),
)

homeautomationpatterns = patterns('',
    url(r'^homeautomation/$', views.HomeAutomationPostGet.as_view()),
    url(r'^homeautomation/(?P<user_name>\w+)/$', homeautomation_list),
    url(r'^homeautomation/(?P<user_name>\w+)/(?P<tag_id>\w+)/$', views.homeautomation_destroy),
)

moodlightpatterns = patterns('',
    url(r'^moodlight/$', views.MoodLightPostGet.as_view()),
    url(r'^moodlight/(?P<user_name>\w+)/$', moodlight_list),
    url(r'^moodlight/(?P<user_name>\w+)/(?P<device_id>\w+)/$', views.destroy_moodlight),
)


stresspatterns = patterns('',
    url(r'^stress/$', views.StressView.as_view()),
    url(r'^stress/(?P<user_name>\w+)/$', views.StressByUser.as_view()),
    url(r'^stress/recent/(?P<user_name>\w+)/$', views.get_stress_recent),
    url(r'^stress/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), stress_list), 
)

bloodoxygenpatterns = patterns('',
                               url(r'^bloodoxygen/$', views.BloodOxygenView.as_view()),
                               url(r'^bloodoxygen/(?P<user_name>\w+)/$', views.BloodOxygenByUser.as_view()),
                               url(r'^bloodoxygen/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), blood_oxygen_list), 
)

bloodpressurepatterns = patterns('',
                                 url(r'^bloodpressure/$', blood_pressure_post_list),
                                 url(r'^bloodpressure/(?P<user_name>\w+)/$', views.BloodPressureByUser.as_view()),
                                 url(r'^bloodpressure/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), blood_pressure_list),) 

graphpatterns = patterns('',
    url(regex = r'^iexpress/heartrate/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = heart_rate_list ),

    url(regex = r'^iexpress/breathingrate/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = breathing_rate_list ),

    url(regex = r'^iexpress/posture/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), 
    view = posture_list ),
    
    url(regex = r'^iexpress/skintemperature/(?P<user_name>\w+)/(?P<start>%s)/(?P<end>%s)/$' % (fmt, fmt), view = skin_temperature_list ),
)

sleep_url_patterns = patterns('',
    url(r'^sleep/', include('sleep.urls')),
)

urlpatterns = patterns('', 
)

urlpatterns += biometricspatterns
urlpatterns += userpatterns 
urlpatterns += notificationpatterns 
#urlpatterns += alertspatterns 
urlpatterns += biometricsprecisepatterns 
urlpatterns += washroompatterns 
urlpatterns += weightpatterns
urlpatterns += eventspatterns
urlpatterns += medicationpatterns
urlpatterns += contactspatterns
urlpatterns += homeautomationpatterns
urlpatterns += moodlightpatterns
urlpatterns += stresspatterns
urlpatterns += bloodoxygenpatterns
urlpatterns += bloodpressurepatterns
urlpatterns += graphpatterns 
urlpatterns += sleep_url_patterns
