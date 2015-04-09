from django.db import models
from django.contrib.auth.models import User

class CuraUser(models.Model):
    #user_id = models.OneToOneField(User) # First Name, Last Name, Password, Email
    user_id = models.CharField(max_length = 300) # First Name, Last Name, Password, Email
    role = models.CharField(blank = True, null = True, max_length = 255)
    phone = models.CharField(blank = True, null = True,  max_length = 255)
    settings = models.CharField(max_length = 255, blank = True, null = True)
    #contacts = models.ManyToManyField('self')

    def __str__(self):
        return str(self.user_id)
        
    def __unicode__(self):
        return self.user_id
    
class Biometrics(models.Model):
    user_id = models.CharField(max_length = 255)
    time_recorded = models.CharField(max_length = 255, null = True, blank = True)
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
