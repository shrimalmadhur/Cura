from django.db import models
from django.contrib.auth.models import User

class CuraUser(models.Model):
    #user_id = models.OneToOneField(User) # First Name, Last Name, Password, Email
    user_name = models.CharField(max_length = 300) # First Name, Last Name, Password, Email
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
