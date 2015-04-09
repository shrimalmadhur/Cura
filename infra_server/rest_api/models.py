from django.db import models
from django.contrib.auth.models import User
    
class CuraUser(models.Model):
    user = models.OneToOneField(User) # First Name, Last Name, Password, Email
    role = models.CharField(max_length = 255)
    
class Biometrics(models.Model):
    #cura_user = models.ForeignKey(CuraUser)
    cura_user = models.CharField(max_length = 255)
    #time_recorded = models.DateTimeField(null = True, blank = True)
    time_recorded = models.CharField(max_length = 255, null = True, blank = True)
    time_received = models.DateTimeField(auto_now = True)
    breathing_rate = models.CharField(max_length = 255, null = True, blank = True) 
    heart_rate = models.CharField(max_length = 255, null = True, blank = True)
    estimated_core_temperature = models.IntegerField(null = True, blank = True)
    ecg = models.CharField(max_length=255, null = True, blank = True)
    posture = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return str(self.cura_user)
        
    def __unicode__(self):
        return self.cura_user

