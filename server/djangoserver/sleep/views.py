from models import *
from serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import datetime
import pytz
import json

class SessionViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = SleepSession.objects.all()
  serializer_class = SessionSerializer

  def retrieve(self, request, pk=None):
    session = get_object_or_404(self.queryset, pk=pk)
    ts_data = [ TSDataSerializer(x).data for x in session.time_series_data.all()]

    data = SessionSerializer(session).data
    data['time_series_data'] = ts_data
    return Response(data)

def parse_date(date):
  try:
    dt = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
    return dt
  except ValueError as e:
    raise ParseError(str(e))

class DayGraph(APIView):

  def get(self, request, *args, **kwargs):
    uid = kwargs['uid']
    dtype = kwargs['dtype']
    date = kwargs['date']
    user = get_object_or_404(User, pk=uid)
    dt = parse_date(date)
    sessions = user.sleepsession_set.filter(session_end__year=dt.year, 
        session_end__month=dt.month, session_end__day=dt.day).order_by('session_end')

    if dtype == 'cycle':
      ret = {'values': []}
      for s in sessions:
        cycles = s.time_series_data.filter(data_type=TSData.TYPE_CYCLE).order_by('timestamp')
        values = [ {'x': c.int_timestamp, 'y': c.value} for c in cycles ]
        ret['values'] = ret['values'] + values
      return Response(ret)
    else:
      raise Http404()


class RangeGraph(APIView):

  def get(self, request, *args, **kwargs):
    uid = kwargs['uid']
    dtype = kwargs['dtype']
    begin = kwargs['begin']
    end = kwargs['end']
    user = get_object_or_404(User, pk=uid)
    dt1 = parse_date(begin)
    dt2 = parse_date(end)
    sessions = user.sleepsession_set.filter(session_end__gte=dt1, session_end__lt=dt2)

    if dtype == 'score':
      scores = [ {'x': s.int_session_end, 'y': s.total_score} for s in sessions ]
      return Response({'values': scores})
    else:
      raise Http404()


