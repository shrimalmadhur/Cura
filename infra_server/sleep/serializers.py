from models import *
from time import mktime
from rest_framework import serializers

class TSDataSerializer(serializers.ModelSerializer):
  timestamp = serializers.SerializerMethodField('int_timestamp')
  
  def int_timestamp(self, obj):
    return int(mktime(obj.timestamp.timetuple()))

  class Meta:
    model = TSData


class SessionSerializer(serializers.ModelSerializer):
  class Meta:
    model = SleepSession
