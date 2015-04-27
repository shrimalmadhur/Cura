from time import mktime
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
  session_start = models.DateTimeField(null=True, blank=True)
  session_end = models.DateTimeField(null=True, blank=True)
  
  sleep_time_target = models.PositiveIntegerField(null=True, blank=True)
  rest_heart_rate = models.PositiveIntegerField(null=True, blank=True)
  avg_respiration_rate = models.FloatField(null=True, blank=True)
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

  @property
  def total_score(self):
    score = self.score_amount_sleep + self.score_sleep_efficiency + self.score_awakening
    score += self.score_awakening + self.score_snoring
    return score

  @property
  def int_session_end(self):
    return int(mktime(self.session_end.timetuple()))

  @property
  def total_sleep_time(self):
    return self.stage_duration_R + self.stage_duration_S

class TSDTypeQS(models.QuerySet):
  def cycles(self):
    return self.filter(data_type=TSData.TYPE_CYCLE).order_by('timestamp')

  def snores(self):
    return self.filter(data_type=TSData.TYPE_SNORE).order_by('timestamp')

  def hearts(self):
    return self.filter(data_type=TSData.TYPE_HEART).order_by('timestamp')

  def presences(self):
    return self.filter(data_type=TSData.TYPE_PRESE).order_by('timestamp')

  def stages(self):
    return self.filter(data_type=TSData.TYPE_STAGE).order_by('timestamp')

class TSDataManager(models.Manager):
  def get_queryset(self):
    return TSDTypeQS(self.model, using=self._db)

  def get_cycles(self):
    return self.get_queryset().cycles()

  def get_snores(self):
    return self.get_queryset().snores()

  def get_hearts(self):
    return self.get_queryset().hearts()

  def get_presences(self):
    return self.get_queryset().presences()

  def get_stages(self):
    return self.get_queryset().stages()


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
      (TYPE_HEART, 'Heart Rate'),
      (TYPE_PRESE, 'Presence'),
  )

  sleep_session = models.ForeignKey(SleepSession, related_name='time_series_data')
  data_type = models.IntegerField(choices=TYPE_CHOICES)
  timestamp = models.DateTimeField()
  value = models.FloatField()

  type_mgr = TSDataManager()

  @property
  def int_timestamp(self):
    return int(mktime(self.timestamp.timetuple()))
