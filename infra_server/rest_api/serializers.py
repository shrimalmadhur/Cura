from models import Biometrics, CuraUser, BiometricsPrecise, Washroom, Weight, HomeAutomation, MoodLight, Stress, Contacts, Medication, Events
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

class WashroomSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)  
    time_recorded = serializers.DateTimeField(required = True)  
    time_received = serializers.DateTimeField(required = False)
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    class Meta:
        model = Washroom 

class WeightSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)  
    time_recorded = serializers.DateTimeField(required = True)  
    time_received = serializers.DateTimeField(required = False)
    weight = serializers.IntegerField()

    class Meta:
        model = Weight 

class HomeAutomationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)  
    tag_id = serializers.CharField(max_length = 255)  
    signal_type = serializers.CharField(max_length = 255)  
    current_value = serializers.IntegerField(required = False)  
    required_value = serializers.IntegerField()  
    mode = serializers.CharField(max_length = 255, required = False)  

    class Meta:
        model = HomeAutomation

class MoodLightSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)
    device_id = serializers.CharField(max_length = 255)
    bridge_ip_address = serializers.CharField(max_length = 255)
    parameter = serializers.CharField(max_length = 255)
    resource1 = serializers.CharField(max_length = 255)
    resource2 = serializers.CharField(max_length = 255)
    message = serializers.CharField(max_length = 255)

    class Meta:
        model = MoodLight

class StressSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)
    stress_score = serializers.DecimalField(required = False, max_digits = 15, decimal_places = 5)
    skin_conductance = serializers.IntegerField(required = False)
    duration = serializers.IntegerField(required = False)
    number_relax_events = serializers.IntegerField(required = False)
    number_stress_events = serializers.IntegerField(required = False)
    number_steady_events = serializers.IntegerField(required = False)
    time_recorded = serializers.DateTimeField(required = True)
    time_received = serializers.DateTimeField(required = False)
    
    class Meta:
        model = Stress

class ContactsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)
    contact_name = serializers.CharField(max_length = 255)
    contact_phone = serializers.CharField(max_length = 255, required = False)
    contact_mail = serializers.CharField(max_length = 255, required = False)
    contact_role = serializers.CharField(max_length = 255)
    contact_comments = serializers.CharField(max_length = 255, required = False)

    class Meta:
        model = Contacts

class MedicationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)
    created_by = serializers.CharField(max_length = 255)
    instructions = serializers.CharField(max_length = 255, required = False)
    schedule = serializers.CharField(max_length = 255, required = False)
    drug_name = serializers.CharField(max_length = 255)
    drug_details = serializers.CharField(max_length = 255)

    class Meta:
        model = Medication

class EventsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length = 255)
    created_by = serializers.CharField(max_length = 255)
    event_type = serializers.CharField(max_length = 255)
    event_time = serializers.DateTimeField(required = True)
    event_linked_users = serializers.CharField(max_length = 255)
    description = serializers.CharField(max_length = 255)

    class Meta:
        model = Events

