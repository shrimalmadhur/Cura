from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_api.models import Biometrics, CuraUser, BiometricsPrecise, Weight
from rest_api.serializers import BiometricsSerializer, CuraUserSerializer, BiometricsPreciseSerializer, WeightSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import httplib

#  Weight #
class PostWeight(generics.CreateAPIView):
    serializer_class = WeightSerializer 

class GetDestroyWeight(generics.RetrieveDestroyAPIView):
    serializer_class = WeightSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return Weight.objects.filter(user_name = user_name)


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
