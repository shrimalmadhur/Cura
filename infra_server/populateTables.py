import os
import datetime
import random
from rest_api.models import ( Biometrics, BiometricsPrecise, BloodPressure )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infra_server.settings")


def populate_bloodpressure():
  for i in xrange(0, 2):
    new_bloodpressure = BloodPressure(user_name = 'mshrimal',
                                      systolic = 120 + random.randint(-10,10)
                                      dystolic = 83 + random.randint(-5,5)
                                      time_recorded = datetime.datetime(2015, 4, 28, 0, i % 15))
    new_bloodpressure.save()

def populate_biometrics(user_name, 
                        time_recorded, 
                        sample_points, 
                        heart_rate = 50,
                        breathing_rate = '50',
                        ecg = '50',
                        estimated_core_temperature = '50',
                        posture = '50'):
  for i in xrange(0, sample_points):
    new_biometric = Biometrics(user_name = user_name,
                               time_recorded = time_recorded,
                               heart_rate = heart_rate,
                               breathing_rate = breathing_rate,
                               ecg = ecg,
                               estimated_core_temperature = estimated_core_temperature,
                               posture = posture)
    new_biometric.save()

if __name__ == '__main__':
  populate_bloodpressure()
