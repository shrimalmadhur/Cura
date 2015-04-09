from models import Biometrics
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(style = {'input_type' : 'password' })
    
class BiometricsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        biometrics = [Biometerics(**item) for item in validated_data]
        return Biometrics.objects.bulk_create(biometrics) 
    
class BiometricsSerializer(serializers.ModelSerializer):
    
    #cura_user = serializers.CharField(max_length = 200)
    #heart_rate = serializers.CharField(max_length = 200)
    
    class Meta:
        model = Biometrics
        list_serializer_class = BiometricsListSerializer
        fields= ('user_id','heart_rate', 'time_recorded', 'time_received', 'breathing_rate', 'ecg', 'estimated_core_temperature', 'posture')
   
