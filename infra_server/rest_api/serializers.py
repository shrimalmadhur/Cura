from models import Biometrics, CuraUser
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
    #cura_user = serializers.CharField(max_length = 200)
    #heart_rate = serializers.CharField(max_length = 200)
    
    class Meta:
        model = Biometrics
        list_serializer_class = BiometricsListSerializer
        fields = ('user_id','heart_rate', 'time_recorded', 'time_received', 'breathing_rate', 'ecg', 'estimated_core_temperature', 'posture')
