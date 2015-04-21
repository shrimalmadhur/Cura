from datetime import datetime
from urllib import urlencode
from models import *
import urllib2
import json
import time
import pytz

def update_sleep(user):
  uc, created = UserCredential.objects.get_or_create(user=user)
  if not (uc.email and uc.password):
    raise ValueError('Missing Email or Password')

  client = BedditClient.get_auth_client(uc.email, uc.password)
  last_session = user.sleepsession_set.last()
  if last_session:
    sleeps = client.get_sleep(after=last_session.date.strftime('%Y-%m-%d'))
  else:
    sleeps = client.get_sleep()

  for sleep in sleeps:
    sleep_to_db(sleep, user)

def sleep_to_db(sleep, user):
  session = SleepSession()
  session.user = user
  tv_tracks = sleep.pop('time_value_tracks')

  session.date = datetime.strptime(sleep.get('date'), '%Y-%m-%d').date()
  session.sleep_time_target = sleep.get('sleep_time_target')
  session.rest_heart_rate = sleep.get('resting_heart_rate')
  session.avg_respiration_rate = sleep.get('average_respiration_rate')
  session.sleep_latency = sleep.get('sleep_latency')
  session.total_snore_duration = sleep.get('total_snoring_episode_duration')
  session.away_count = sleep.get('away_episode_count')

  session.stage_duration_A = sleep.get('stage_duration_A')
  session.stage_duration_S = sleep.get('stage_duration_S')
  session.stage_duration_R = sleep.get('stage_duration_R')
  session.stage_duration_W = sleep.get('stage_duration_W')
  session.stage_duration_G = sleep.get('stage_duration_G')

  session.score_amount_sleep = sleep.get('score_amount_of_sleep')
  session.score_bed_exits = sleep.get('score_bed_exits')
  session.score_snoring = sleep.get('score_snoring')
  session.score_sleep_latency = sleep.get('score_sleep_latency')
  session.score_sleep_efficiency = sleep.get('score_sleep_efficiency')
  session.score_awakening = sleep.get('score_awakenings')
  session.save()
  
  tz = pytz.timezone(sleep.get('timezone'))
  tv_tracks_to_db(tv_tracks, session, tz)

def tv_tracks_to_db(tv_tracks, session, tz):

  dtypes = {
      u'sleep_cycles': TSData.TYPE_CYCLE, 
      u'heart_rate_curve': TSData.TYPE_HEART, 
      u'snoring_episodes': TSData.TYPE_SNORE, 
      u'sleep_stages': TSData.TYPE_STAGE,
      u'presence': TSData.TYPE_PRESE, 
  }

  for k in tv_tracks.keys():
    data_type = dtypes[k]
    for d in tv_tracks[k]['items']:
      try:
        data = TSData(sleep_session=session, data_type=data_type)
        data.timestamp = datetime.utcfromtimestamp(d[0]).replace(tzinfo=tz)
        data.value = float(d[1])
        data.save()
      except ValueError:
        pass


class BedditClient(object):

  BASE_URL = 'https://cloudapi.beddit.com'

  def __init__(self, u_id, token):
    if not u_id:
      raise ValueError('Missing Argument: u_id')
    if not token:
      raise ValueError('Missing Argument: token')

    self.u_id = u_id
    self.token = token

  @classmethod
  def get_auth_client(cls, email, pwd):
    url = cls.BASE_URL + '/api/v1/auth/authorize'
    params = {
        'grant_type': 'password',
        'username': email,
        'password': pwd,
    }
    req = urllib2.Request(url, urlencode(params))
    resp = json.loads(urllib2.urlopen(req).read())
    return BedditClient(resp.get('user'), resp.get('access_token'))


  def get_sleep(self, after=None, start=None, end=None, reverse=None, limit=None):
    """Get sleep resource as a list of sleep data dictionary

    Keywords arguments:
    after -- filter sleep data after given date with format '2015-01-01'
    start -- filter sleep data between start and end date with format '2015-01-01'
    end -- use with start; won't be used if 'after' argument is given
    reverse -- 'yes' if reverse chronological order is preferred. Default: 'no'
    limit -- max number of return results (integer)
    """
    url = self.BASE_URL + '/api/v1/user/%s/sleep?' % self.u_id

    params = {}
    if reverse == 'yes':
      params['reverse'] = 'yes'
    if limit > 0:
      params['limit'] = limit
    if after:
      params['updated_after'] = time.mktime(time.strptime(after, '%Y-%m-%d'))
    elif start and end:
      params['start_date'] = start
      params['end_date'] = end

    url += urlencode(params)
    req = urllib2.Request(url)
    req.add_header('Authorization', 'UserToken %s' % self.token)
    return json.loads(urllib2.urlopen(req).read())

