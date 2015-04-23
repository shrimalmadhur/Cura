from django.db import models
from django.contrib.auth.models import User

class CuraUser(models.Model):
    #user_id = models.OneToOneField(User) # First Name, Last Name, Password, Email
    #user_name = models.CharField(max_length = 300) # First Name, Last Name, Password, Email
    mail = models.CharField(max_length = 255)  
    role = models.CharField(blank = True, null = True, max_length = 255)
    phone = models.CharField(blank = True, null = True,  max_length = 255)
    settings = models.CharField(max_length = 255, blank = True, null = True)
    #contacts = models.ManyToManyField('self')

    def __str__(self):
        return str(self.user_id)
        
    def __unicode__(self):
        return self.user_id

class Biometrics(models.Model):
    user_name = models.CharField(max_length = 255)
    time_recorded = models.DateTimeField(null = True, blank = True)
    time_received = models.DateTimeField(auto_now = True)
    breathing_rate = models.CharField(max_length = 255, null = True, blank = True) 
    heart_rate = models.CharField(max_length = 255, null = True, blank = True)
    estimated_core_temperature = models.IntegerField(null = True, blank = True)
    ecg = models.CharField(max_length=255, null = True, blank = True)
    posture = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return str(self.user_id)
        
    def __unicode__(self):
        return self.user_id

class BiometricsPrecise(models.Model):

    RECORD_CHOICES = ((0, 'ECG'), (1, 'BREATH')) 

    user_name = models.CharField(max_length = 255)
    record_type = models.CharField(max_length = 255, choices = RECORD_CHOICES)
    time_recorded = models.DateTimeField(null = True, blank = True)
    time_received = models.DateTimeField(auto_now = True)
    sequence_number = models.CharField(max_length = 100, blank = True, null = True)
    timestamp_year = models.IntegerField(null = True)
    timestamp_month = models.IntegerField(null = True)
    timestamp_msofday = models.IntegerField(null = True)
    samples_per_packet = models.IntegerField(null = True)
    samples = models.CharField(max_length = 100, blank = True, null = True)

class Washroom(models.Model):
    user_name = models.CharField(max_length = 255)
    time_recorded = models.DateTimeField()
    time_received = models.DateTimeField(auto_now = True)
    start = models.DateTimeField()
    end = models.DateTimeField()

class Weight(models.Model):
    user_name = models.CharField(max_length = 255)
    time_recorded = models.DateTimeField()
    time_received = models.DateTimeField(auto_now = True)
    weight = models.IntegerField()

class HomeAutomation(models.Model):
    user_name = models.CharField(max_length = 255)
    tag_id = models.CharField(max_length = 255)
    signal_type = models.CharField(max_length = 255)
    current_value = models.CharField(max_length = 10)
    required_value = models.CharField(max_length = 10)
    mode = models.CharField(max_length = 255)

class MoodLight(models.Model):
    user_name = models.CharField(max_length = 255)
    device_id = models.CharField(max_length = 255)
    bridge_ip_address = models.CharField(max_length = 255)
    parameter = models.CharField(max_length = 255)
    resource1 = models.CharField(max_length = 255)
    resource2 = models.CharField(max_length = 255)
    message = models.CharField(max_length = 255)

class Stress(models.Model):
    user_name = models.CharField(max_length = 255)
    stress_score = models.DecimalField( max_digits = 15, decimal_places = 5)
    skin_conductance = models.IntegerField()
    duration = models.IntegerField()
    number_relax_events = models.IntegerField()
    number_stress_events = models.IntegerField()
    number_steady_events = models.IntegerField()
    time_recorded = models.DateTimeField()
    time_received = models.DateTimeField(auto_now = True)

class Contacts(models.Model):
    user_name = models.CharField(max_length = 255)
    contact_name = models.CharField(max_length = 255)
    contact_phone = models.CharField(max_length = 255)
    contact_mail = models.CharField(max_length = 255)
    contact_role = models.CharField(max_length = 255)
    contact_comments = models.CharField(max_length = 255)

class Medication(models.Model):
    user_name = models.CharField(max_length = 255)
    created_by = models.CharField(max_length = 255)
    instructions = models.CharField(max_length = 255)
    schedule = models.CharField(max_length = 255)
    drug_name = models.CharField(max_length = 255)
    drug_details = models.CharField(max_length = 255)

class Events(models.Model):
    user_name = models.CharField(max_length = 255)
    created_by = models.CharField(max_length = 255)
    event_type = models.CharField(max_length = 255)
    event_time = models.DateTimeField()
    event_linked_users = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
