from models import Biometrics, CuraUser, BiometricsPrecise, Washroom
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class CuraUserSerializer(serializers.ModelSerializer): 
    user_name = serializers.CharField(max_length = 255)  
    mail = serializers.CharField(max_length = 255, required = False)  
    #user_id = UserSerializer()
    role = serializers.CharField(max_length = 255, required = False)
    phone = serializers.CharField(max_length = 255, required = False)
    settings = serializers.CharField(max_length = 255, required = False)

    class Meta:
        model = CuraUser
        fields = ('user_name', 'mail', 'role', 'phone', 'settings')

class BiometricsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        biometrics = [ Biometerics(**item) for item in validated_data ]
        return Biometrics.objects.bulk_create(biometrics) 
    
class BiometricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biometrics
        list_serializer_class = BiometricsListSerializer
        fields = ('user_name','heart_rate', 'time_recorded', 'time_received', 'breathing_rate', 'ecg', 'estimated_core_temperature', 'posture')

class BiometricsPreciseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)  
    record_type = serializers.CharField(max_length = 255, required = True)  
    time_recorded = serializers.DateTimeField(required = False)  
    time_received = serializers.DateTimeField(required = False)
    sequence_number = serializers.CharField(required = False)
    timestamp_year = serializers.IntegerField(required = False)
    timestamp_month = serializers.IntegerField(required = False)
    timestamp_msofday = serializers.IntegerField(required = False)
    samples_per_packet = serializers.IntegerField(required = False)

    class Meta:
        model = BiometricsPrecise

class WeightSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)  
    time_recorded = serializers.DateTimeField(required = False)  
    time_received = serializers.DateTimeField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    class Meta:
        model = Washroom 
