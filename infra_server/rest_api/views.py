from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_api.models import Biometrics, CuraUser
from rest_api.serializers import BiometricsSerializer, CuraUserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import httplib

# Push Notification #
@api_view(['POST'])
@csrf_exempt
def notify(request):
    user_name = request.POST['user_name']
    data = request.POST['data']

    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/push', json.dumps({
           "where": {
               'curaUser' : user_name
           },
           "data": {
               "xyz" : "data"
           }
         }), {
           "X-Parse-Application-Id": "UBBIKb8y8RqzSsoXXJS6iCO7D2Idb1HNk2XUcmA0",
           "X-Parse-REST-API-Key": "uhA6OWZl6zp21UM6A5eSAfXipu2tYN9wqyx6LnSt",
           "Content-Type": "application/json"
         })
    print ("Success")
    result = json.loads(connection.getresponse().read())
    print ("Result " , result)
    return Response("Success")

# Cura Users #
# api/v1/users/(userId) - GET PUT DELETE
class GetUser(generics.ListCreateAPIView):
    serializer_class = CuraUserSerializer 

    def get_queryset(self):
        return CuraUser.objects.all()

# Biometrics #
class GetCuraUser(generics.ListAPIView):
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

'''
@csrf_exempt
@api_view(['POST'])
def populate_table(request):

    if request.method == 'POST':
        # Cura User -> User
        # Biometrics
        # Built in User #
        #user = User(username = request.POST['username'])
        #user.set_password(request.POST['password'])
        #user.save()
        
        # Cura User - save #
        #cura_user = CuraUser(user = user, role = 'Patient')
        #cura_user.save()
        
        # Biometrics #
        
        biometric = Biometrics(user_id = request.POST['user_id'],
                               heart_rate = request.POST['heart_rate'],
                               time_recorded = request.POST['time_recorded'],
                               breathing_rate = request.POST['breathing_rate'],
                               ecg = request.POST['ecg'],
                               estimated_core_temperature = request.POST['estimated_core_temperature'],
                               posture = request.POST['posture'])                          
        biometric.save()
        return Response(json.dumps("Tables Populated"))
'''
