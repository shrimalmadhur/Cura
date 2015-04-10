from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_api.models import Biometrics, CuraUser
from rest_api.serializers import BiometricsSerializer, CuraUserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Cura Users #

# api/v1/users/(userId) - GET PUT DELETE
class GetUser(generics.ListCreateAPIView):
    serializer_class = CuraUserSerializer 

    def get_queryset(self):
        return CuraUser.objects.all()

# Biometrics #
@csrf_exempt
@api_view(['GET'])
def resource_get(request):
    if request.method == 'GET':
        biometrics = Biometrics.objects.all()
        json_dump = json.dumps([str(obj) for obj in Biometrics.objects.values()])
        #biometrics = BiometricsSerializer(biometrics, many = True)
        return Response(json_dump)

class GetCuraUser(generics.ListAPIView):
    serializer_class = BiometricsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Biometrics.objects.filter(user_id = user_id)

class GetBiometricsData(generics.ListAPIView):
    serializer_class = BiometricsSerializer

    def get_queryset(self):
        return Biometrics.objects.all()

class GetTimeUser(generics.ListAPIView):
    serializer_class = BiometricsSerializer

    # Fix this #
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        start_time = self.kwargs['start']
        end_time = self.kwargs['end']
        filtered_objects = Biometrics.objects.filter(user_id = user_id)
        filtered_objects = filtered_objects.filter(time_recorded__gte = start_time, time_recorded__lte = end_time)
        return filtered_objects

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
