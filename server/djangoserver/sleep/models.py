from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import EncryptedTextField

class UserCredential(models.Model):
  user = models.OneToOneField(User, primary_key=True, related_name='beddit_credential')
  email = models.EmailField(max_length=254) # email use for beddit account
  password = EncryptedTextField() # don't have spec of max limit of beddit password
    

class SleepSession(models.Model):
  user = models.ForeignKey(User)
  date = models.DateField()
  
  sleep_time_target = models.PositiveIntegerField(null=True, blank=True)
  rest_heart_rate = models.PositiveIntegerField(null=True, blank=True)
  avg_respiration_rate =models.PositiveSmallIntegerField(null=True, blank=True)
  sleep_latency = models.PositiveIntegerField(null=True, blank=True)
  total_snore_duration = models.PositiveIntegerField(null=True, blank=True)
  away_count = models.PositiveSmallIntegerField(null=True, blank=True)
  bath_count = models.PositiveSmallIntegerField(default=0)

  stage_duration_A = models.PositiveIntegerField(null=True, blank=True)
  stage_duration_S = models.PositiveIntegerField(null=True, blank=True)
  stage_duration_R = models.PositiveIntegerField(null=True, blank=True)
  stage_duration_W = models.PositiveIntegerField(null=True, blank=True)
  stage_duration_G = models.PositiveIntegerField(null=True, blank=True)

  score_amount_sleep = models.SmallIntegerField(null=True, blank=True)
  score_bed_exits = models.SmallIntegerField(null=True, blank=True)
  score_snoring = models.SmallIntegerField(null=True, blank=True)
  score_sleep_latency = models.SmallIntegerField(null=True, blank=True)
  score_sleep_efficiency = models.SmallIntegerField(null=True, blank=True)
  score_awakening = models.SmallIntegerField(null=True, blank=True)


# timeseries data from beddit
class TSData(models.Model):
  TYPE_STAGE = 1
  TYPE_SNORE = 2
  TYPE_CYCLE = 3
  TYPE_HEART = 4
  TYPE_PRESE = 5
  TYPE_CHOICES = (
      (TYPE_STAGE, 'Sleep Stage'),
      (TYPE_SNORE, 'Snoring Episode'),
      (TYPE_CYCLE, 'Sleep Cycle'),
      (TYPE_CYCLE, 'Heart Rate'),
      (TYPE_PRESE, 'Presence'),
  )

  sleep_session = models.ForeignKey(SleepSession)
  data_type = models.IntegerField(choices=TYPE_CHOICES)
  timestamp = models.DateTimeField()
  value = models.FloatField()

