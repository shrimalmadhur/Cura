from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout 
from rest_api.models import (Biometrics, CuraUser, BiometricsPrecise, Weight, Washroom, HomeAutomation, MoodLight, Stress, Events, Medication, Contacts, BloodOxygen, BloodPressure)
from rest_api.serializers import (BiometricsSerializer, CuraUserSerializer, BiometricsPreciseSerializer, WeightSerializer, WashroomSerializer, HomeAutomationSerializer, MoodLightSerializer, StressSerializer, EventsSerializer, MedicationSerializer,ContactsSerializer, BloodOxygenSerializer, BloodPressureSerializer, ) 
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
import json
import ast
from datetime import datetime
import httplib

### Home Automation Demo Changes ###
import httplib
import requests
import time
from requests.auth import HTTPBasicAuth

def parse_date(date):
    try:
        dt = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        return dt
    except ValueError as e:
        raise ParseError(str(e))

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
class GetWeight(generics.ListAPIView):
    serializer_class = WeightSerializer 

    def get_queryset(self):
        return Weight.objects.filter(user_name = self.kwargs['user_name'])

class PostWeight(generics.CreateAPIView):
    serializer_class = WeightSerializer 

#  Washroom #
class WashroomPost(generics.CreateAPIView):
    serializer_class = WashroomSerializer 

class WashroomGetDestroy(generics.ListAPIView):
    serializer_class = WashroomSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return Washroom.objects.filter(user_name = user_name)

# Biometrics Precise #
class GetBiometricsPrecise(generics.ListAPIView):
    serializer_class = BiometricsPreciseSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = BiometricsPrecise
        return BiometricsPrecise.objects.filter(user_name = user_name)

        #char_to_dict = ast.literal_eval( request.data['samples'] ) 
        #validated_data['samples'] = json.dumps( char_to_dict )
        #io = StringIO()
        #validated_data['samples'] = json.dumps(validated_data['samples'], io)
           
class PostBiometricsPrecise(generics.CreateAPIView):
    serializer_class = BiometricsPreciseSerializer 

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

# api/v1/users/- GET PUT DELETE
class User(viewsets.ModelViewSet):
    serializer_class = CuraUser 

    def get_queryset(self):
        return CuraUser.objects.filter(user_name = self.kwargs['user_name']) 

    def list(self, request, user_name):
        result = self.get_queryset() 
        json_result = CuraUserSerializer(result, many = True)
        return Response(json_result.data)

    def update(self, request, user_name):
        result = HomeAutomation.objects.get(user_name = user_name)
        
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

        json_result = CuraUserSerializer(result)
        return Response(json_result.data)

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

class GetBiometricsTimeUser(generics.ListAPIView):
    serializer_class = BiometricsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_name']
        start_time = self.kwargs['start']
        end_time = self.kwargs['end']
        
        print "start time ", start_time
        print "end time ",  end_time 

        start_time = datetime.strptime(start_time, '%Y-%m-%d')
        end_time = datetime.strptime(end_time, '%Y-%m-%d')

        filtered_objects = Biometrics.objects.filter(user_name = user_name)
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
        ### ha demo changes ###
        ###device = '115341'
        ###required_value = '1'
        ###mode = ''

        device = request.data['tag_id']
        required_value = request.data['required_value']
        mode = request.data['mode']

        ip_addr = 'http://128.2.82.2:25105/3?0262'
        tag1 = '1155B6'
        tag2 = '115341'
        tag3 = '115914'
        tag4 = '115498'
        tag_thermo = '11B264'

        sd_flag = '0F'
        level = 'FF'

        state_on = '11'
        state_off = '13'

        hops = '=I=3'
        if mode == 'hot':
            required_value1 = '6B'
            required_value2 = '6D'
            level1 = '04'

        elif mode == 'cold':
            required_value1 = '6B'
            required_value2 = '6C'
            level1 = '05'


        if device == tag_thermo:
            req1 = ip_addr + tag_thermo + sd_flag + required_value1 + level1 + hops
            print req1
            for i in range (1,3):
                r = requests.get(req1,auth=HTTPBasicAuth('Guinever','HYXzAfQN'))
                time.sleep(0.5);
            
            req = ip_addr + tag_thermo + sd_flag + required_value2 + required_value + hops
            print req
        
        if required_value == '1':
            required_value = state_on
            
        elif required_value == '0':
            required_value = state_off

        if device == tag1:
            req = ip_addr + tag1 + sd_flag + required_value + level + hops
            print req
                            
        elif device == tag2:
            req = ip_addr + tag2 + sd_flag + required_value + level + hops
            print req
                                    
        elif device == tag3:
            req = ip_addr + tag3 + sd_flag + required_value + level + hops
            print req
                                            
        elif device == tag4:
            req = ip_addr + tag4 + sd_flag + required_value + level + hops
            print req
                                                    
        elif device == tag_thermo:
            ### req = ip_addr + tag_thermo + sd_flag +
            print req

        for i in range (1,3):
            r = requests.get(req,auth=HTTPBasicAuth('Guinever', 'HYXzAfQN'))
            time.sleep(0.5);

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
class StressGetTime(viewsets.ViewSet):

    def list(self, request, user_name, start, end):
        if start != end:
            start = datetime.strptime(start, '%Y-%m-%d')
            end = datetime.strptime(end, '%Y-%m-%d')
            result = Stress.objects.filter(user_name = user_name) 
            result = result.filter(time_recorded__gte = start, time_recorded__lte = end)
            serialized = StressSerializer( result, many = True)
            return Response( serialized.data )
        else:
            start = datetime.strptime(start, '%Y-%m-%d')
            end = datetime.strptime(end, '%Y-%m-%d')
            end = end.replace(hour = 23, minute = 59)
            result = Stress.objects.filter(time_recorded__gte = start, time_recorded__lte = end)
            serialized = StressSerializer( result, many = True)
            return Response( serialized.data )

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

# Blood Oxygen #
class BloodOxygenView(generics.ListCreateAPIView):
    serializer_class = BloodOxygenSerializer
    
    def get_queryset(self):
        return BloodOxygen.objects.all()

class BloodOxygenByUser(generics.ListAPIView):
    serializer_class = BloodOxygenSerializer
    lookup_field = 'user_name'
    
    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = BloodOxygen.objects.filter(user_name = user_name)
        return result

# Blood Pressure #
class BloodPressureView(generics.ListCreateAPIView):
    serializer_class = BloodPressureSerializer
    
    def get_queryset(self):
        return BloodPressure.objects.all()

class BloodPressureByUser(generics.ListAPIView):
    serializer_class = BloodPressureSerializer
    lookup_field = 'user_name'
    
    def get_queryset(self):
        user_name = self.kwargs['user_name']
        result = BloodPressure.objects.filter(user_name = user_name)
        return result
