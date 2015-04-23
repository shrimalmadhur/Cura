from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_api.models import (Biometrics, CuraUser, BiometricsPrecise, Weight, Washroom, HomeAutomation, Stress, Events, Medication, Contacts)
from rest_api.serializers import (BiometricsSerializer, CuraUserSerializer, BiometricsPreciseSerializer,
        WeightSerializer, WashroomSerializer, HomeAutomationSerializer, StressSerializer, EventsSerializer, MedicationSerializer,ContactsSerializer)
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import httplib


### Events ###

# api/v1/events/#
class EventsPost(generics.CreateAPIView):
    serializer_class = EventsSerializer

# api/v1/events/(userId) #
class EventsByUser(generics.ListAPIView):
    serializer_class = EventsSerializer
    lookup_field = 'user_name'
    
    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = Events.objects.filter(user_name = user_name)
        return result

# Put/Delete based on id /medication_id
#class EventsPutDestroy(APIView):
    
    #def delete(self, request, id):
    #result = Events.objects.get(id = id)
    #    result.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)


### Medication ###

# api/v1/medication (POST) #
class MedicationPost(generics.CreateAPIView):
    serializer_class = MedicationSerializer

# api/v1/medication/(userId) #
class MedicationByUser(generics.ListAPIView):
    serializer_class = MedicationSerializer
    lookup_field = 'user_name'
    
    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = Medication.objects.filter(user_name = user_name)
        return result

### Contacts ###

# api/v1/contacts/ (POST) #
class ContactsPost(generics.CreateAPIView):
    serializer_class = ContactsSerializer

# api/v1/contacts/(userId)  (GET) #
class ContactsByUser(generics.ListAPIView):
    serializer_class = ContactsSerializer
    lookup_field = 'user_name'
    
    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = Contacts.objects.filter(user_name = user_name)
        return result

#  Weight #
class WeightPost(generics.CreateAPIView):
    serializer_class = WeightSerializer 

class WeightGetDestroy(APIView):
    
    def get(self, request, user_name):
        result = Weight.objects.filter(user_name = user_name)
        serialized = WeightSerializer(result)
        return Response(serialized)

    def delete(self, request, user_name):
        result = Weight.objects.get(user_name = user_name)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  Washroom #
class WashroomPost(generics.CreateAPIView):
    serializer_class = WashroomSerializer 

class WashroomGetDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = WashroomSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return Washroom.objects.filter(user_name = user_name)

# Biometrics Precise #
class GetBiometricsPrecise(generics.ListAPIView):
    serializer_class = BiometricsPreciseSerializer 

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return BiometricsPrecise.objects.filter(user_name = user_name)

class PostBiometricsPrecise(generics.CreateAPIView):
    serializer_class = BiometricsPreciseSerializer 

@api_view(['GET'])
@csrf_exempt
def get_biometrics_precise(request):
    if request.method == 'GET':
        query = BiometricsPrecise.objects.filter(user_name = user_name)
        if len(query) < 1:
            return Response('Invalid user')
        query = query[0]
        json_response = BiometricsPreciseSerializer(query)
        return Response(json_response)

# Push Notification #
@api_view(['POST'])
@csrf_exempt
def notify(request):
    user_name = request.POST['user_name']
    signal_type = request.POST['signal_type']
    tag_id = request.POST['tag_id'] 
    required_value = int(request.POST['required_value'])

    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/push', json.dumps({
           "where": {
               'curaUser' : user_name
           },
           "data": {
               "user_name" : user_name,
               "signal_type" : signal_type,
               "tag_id" : tag_id,
               "required_value" : required_value
           }
         }), {
           "X-Parse-Application-Id": "UBBIKb8y8RqzSsoXXJS6iCO7D2Idb1HNk2XUcmA0",
           "X-Parse-REST-API-Key": "uhA6OWZl6zp21UM6A5eSAfXipu2tYN9wqyx6LnSt",
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    return Response("Success")

# Cura Users #
# api/v1/users/(userId) - GET PUT DELETE
class GetUser(generics.ListCreateAPIView):
    '''
    Function to get and post to the CuraUser
    '''
    serializer_class = CuraUserSerializer 

    def get_queryset(self):
        return CuraUser.objects.all()

# Biometrics #
class GetCuraUser(generics.ListAPIView):
    '''
    Function to get the Biometrics Data
    '''
    serializer_class = BiometricsSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return Biometrics.objects.filter(user_name= user_name)

class GetBiometricsData(generics.CreateAPIView):
    serializer_class = BiometricsSerializer

    def get_queryset(self):
        return Biometrics.objects.all()

class GetTimeUser(generics.ListAPIView):
    serializer_class = BiometricsSerializer

    # Fix this #
    def get_queryset(self):
        user_id = self.kwargs['user_name']
        start_time = self.kwargs['start']
        end_time = self.kwargs['end']
        filtered_objects = Biometrics.objects.filter(user_name= user_name)
        filtered_objects = filtered_objects.filter(time_recorded__gte = start_time, time_recorded__lte = end_time)
        return filtered_objects

# Home Automation #
class HomeAutomationPostGet(generics.ListCreateAPIView):
    serializer_class = HomeAutomationSerializer 

    def get_queryset(self):
        return HomeAutomation.objects.all()

'''
class HomeAutomationGetPutDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeAutomationSerializer 
    lookup_field = 'user_name'
    allowed_methods = 'delete'

    def get_queryset(self):
        return HomeAutomation.objects.filter(user_name = self.kwargs['user_name'])
'''

# Home Automation - User Based #
class HomeAutomation(viewsets.ViewSet):

    def list(self, request, user_name):
        result = HomeAutomation.objects.filter(user_name = user_name)
        json_result = HomeAutomationSerializer(result, many = True)
        return Response(json.data)

@api_view(['POST', 'PUT', 'GET'])
@csrf_exempt
def home_automation_user_update(request, user_name):

    if request.method == 'GET':
        result = HomeAutomation.objects.filter(user_name = user_name)
        return Response(HomeAutomationSerializer(result, many = True))

    if request.method == 'PUT':
    

    if request.method == 'DELETE':
        pass

class HomeAutomationUserUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = HomeAutomationSerializer
    lookup_field = 'user_name'

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = HomeAutomation.objects.filter(user_name = user_name)
        return result

# Stress #
class StressView(generics.ListCreateAPIView):
    serializer_class = StressSerializer

    def get_queryset(self):
        return Stress.objects.all()

class StressByUser(generics.ListAPIView):
    serializer_class = StressSerializer
    lookup_field = 'user_name'

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = Stress.objects.filter(user_name = user_name)
        return result
