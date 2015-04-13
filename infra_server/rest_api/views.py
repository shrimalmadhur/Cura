from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_api.models import (Biometrics, CuraUser, BiometricsPrecise, Weight, Washroom, HomeAutomation, MoodLight, Stress, Events, Medication, Contacts)
from rest_api.serializers import (BiometricsSerializer, CuraUserSerializer, BiometricsPreciseSerializer, WeightSerializer, WashroomSerializer, HomeAutomationSerializer, MoodLightSerializer, StressSerializer, EventsSerializer, MedicationSerializer,ContactsSerializer)
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import httplib

### Events ###

class EventsPostGet(generics.ListCreateAPIView):
    serializer_class = EventsSerializer 

    def get_queryset(self):
        return Events.objects.all()

class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer 

    def get_queryset(self):
        return Events.objects.filter(user_name = self.kwargs['user_name'])

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = EventsSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = Events.objects.get(id = int(request.data['id']))
        
        created_by = result.created_by
        event_type = result.event_type
        event_time = result.event_time
        event_linked_users = result.event_linked_users
        description = result.description

        if 'created_by' in request.data:
            created_by = request.data['created_by']

        if 'event_type' in request.data:
            event_type = request.data['event_type']
        
        '''
        if 'event_time' in request.data:
            event_time = request.data['event_time']
        '''

        if 'event_linked_users' in request.data:
            event_linked_users = request.data['event_linked_users']

        if 'description' in request.data:
            description = request.data['description']

        result.created_by = created_by
        result.event_type = event_type
        result.event_time = event_time
        result.event_linked_users = event_linked_users
        result.description = description
        result.save()

        json_result = EventsSerializer(result)
        return Response(json_result.data)

@api_view(['DELETE'])
def destroy_event(request, user_name, pk):
    result = Events.objects.get(user_name = user_name, pk = pk)
    result.delete()
    return Response("Deleted Successfully")

### Medication ###

# api/v1/medication (POST) #
# Home Automation #
class MedicationPostGet(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer 

    def get_queryset(self):
        return Medication.objects.all()

class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer 

    def get_queryset(self):
        return Medication.objects.filter(user_name = self.kwargs['user_name'])

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = MedicationSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = Medication.objects.get(id = int(request.data['id']))

        created_by = result.created_by
        instructions = result.instructions
        schedule = result.schedule 
        drug_name = result.drug_name
        drug_details = result.drug_details

        if 'created_by' in request.data:
            created_by = request.data['created_by']

        if 'instructions' in request.data:
            instructions = request.data['instructions']

        if 'schedule' in request.data:
            schedule = request.data['schedule']

        if 'drug_name' in request.data:
            drug_name = request.data['drug_name']

        if 'drug_details' in request.data:
            drug_details = request.data['drug_details']

        result.created_by = created_by
        result.instructions = instructions
        result.schedule = schedule
        result.drug_name = drug_name
        result.drug_details = drug_details
        result.save()

        json_result = MedicationSerializer(result)
        return Response(json_result.data)

@api_view(['DELETE'])
def destroy_medications(request, user_name, pk):
    result = Medication.objects.get(user_name = user_name, pk = pk)
    result.delete()
    return Response("Deleted Successfully")

### Contacts ###
class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer 

    def get_queryset(self):
        return Contacts.objects.filter(user_name = self.kwargs['user_name'])

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = ContactsSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = Contacts.objects.get(id = int(request.data['id']))

        contact_phone = result.contact_phone
        contact_mail = result.contact_mail
        contact_comments = result.contact_comments

        if 'contact_phone' in request.data:
            contact_phone = request.data['contact_phone']

        if 'contact_mail' in request.data:
            contact_mail = request.data['contact_mail'] 

        if 'contact_comments' in request.data:
            contact_comments = request.data['contact_comments']

        result.contact_name = request.data['contact_name']
        result.contact_role = request.data['contact_role']
        result.contact_phone = contact_phone
        result.contact_mail = contact_mail
        result.contact_comments = contact_comments
        result.save()
        return Response("Successfully Updated")

@api_view(['DELETE'])
def destroy_contact(request, user_name, pk):
    result = Contacts.objects.get(user_name = user_name, pk = pk)
    result.delete()
    return Response("Deleted Successfully")

# api/v1/contacts/ (POST) #
class ContactsPost(generics.ListCreateAPIView):
    queryset = Contacts.objects.all() 
    serializer_class = ContactsSerializer

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

class HomeAutomationViewSet(viewsets.ModelViewSet):
    serializer_class = HomeAutomationSerializer 

    def get_queryset(self):
        return HomeAutomation.objects.filter(user_name = self.kwargs['user_name'])

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = HomeAutomationSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = HomeAutomation.objects.get(user_name = user_name, tag_id = request.data['tag_id'])
        
        current_value = result.current_value
        mode = result.mode

        if 'current_value' in request.data:
                current_value = request.data['current_value']
        if 'mode' in request.data:
                mode = request.data['mode']

        result.signal_type = request.data['signal_type']
        result.current_value = current_value
        result.required_value = request.data['required_value']
        result.mode = mode 
        result.save()

        json_result = HomeAutomationSerializer(result)
        return Response(json_result.data)

@api_view(['DELETE'])
def homeautomation_destroy(request, user_name, tag_id):
    result = HomeAutomation.objects.get(user_name = user_name, tag_id = tag_id) 
    result.delete()
    return Response("Deleted Successfully")

# Mood Light #
class MoodLightPostGet(generics.ListCreateAPIView):
    serializer_class = MoodLightSerializer 

    def get_queryset(self):
        return MoodLight.objects.all()

class MoodLightViewSet(viewsets.ModelViewSet):
    serializer_class = MoodLightSerializer 

    def get_queryset(self):
        return MoodLight.objects.filter(user_name = self.kwargs['user_name'])

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = MoodLightSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = MoodLight.objects.get(user_name = user_name, device_id = request.data['device_id'])
        
        '''
        current_value = result.current_value
        mode = result.mode

        if 'current_value' in request.data:
                current_value = request.data['current_value']
        if 'mode' in request.data:
                mode = request.data['mode']
        '''
        result.bridge_ip_address = request.data['bridge_ip_address']
        result.parameter = request.data['parameter']
        result.resource1 = request.data['resource1']
        result.resource2 = request.data['resource2']
        result.message = request.data['message'] 
        result.save()

        json_result = MoodLightSerializer(result)
        return Response(json_result.data)

@api_view(['DELETE'])
def destroy_moodlight(request, user_name, device_id):
    result = MoodLight.objects.get(user_name = user_name, device_id = device_id)
    result.delete()
    return Response("Deleted Successfully")


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
