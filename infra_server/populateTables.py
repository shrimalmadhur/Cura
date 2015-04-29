import os
import datetime
from rest_api.models import ( Biometrics, BiometricsPrecise )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infra_server.settings")


def populate_bloodpressure(user_name,
                           time_recorded,
                           sample_points,


                           
):

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

f __name__ == '__main__':
  populate_biometrics(user_name = 'moko', 
                      time_recorded = datetime.date(2015, 4, 12), 
                      sample_points = 2)
