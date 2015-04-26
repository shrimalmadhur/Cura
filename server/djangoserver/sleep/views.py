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
import itertools
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
    return prepare_response(dtype, sessions)

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
    return prepare_response(dtype, sessions)

def prepare_response(dtype, sessions):
  ret = {'values': [], 'key': dtype}
  if dtype == 'cycle':
    for s in sessions:
      cycles = s.time_series_data(manager='type_mgr').get_cycles()
      values = [ {'x': c.int_timestamp, 'y': c.value} for c in cycles ]
      ret['values'] = ret['values'] + values
    return Response([ret])
  elif dtype == 'heart':
    for s in sessions:
      hrs = s.time_series_data(manager='type_mgr').get_hearts()
      values = [ {'x': h.int_timestamp, 'y': h.value} for h in hrs ]
      ret['values'] = ret['values'] + values
    return Response([ret])
  elif dtype == 'stage':
    for s in sessions:
      stages = s.time_series_data(manager='type_mgr').get_stages()
      values = [ {'x': st.int_timestamp, 'y': st.value} for st in stages ]
      ret['values'] = ret['values'] + values
    return Response([ret])
  elif dtype == 'snore':
    for s in sessions:
      snores = s.time_series_data(manager='type_mgr').get_snores()
      values = [ {'x': sn.int_timestamp, 'y': sn.value} for sn in snores ]
      ret['values'] = ret['values'] + values
    return Response([ret])
  elif dtype == 'score':
    scores = [ {'x': s.int_session_end, 'y': s.total_score} for s in sessions ]
    return Response({'values': scores})
  elif dtype == 'rest':
    values = [ {'x': s.int_session_end, 'y': s.rest_heart_rate} for s in sessions]
    return Response({'values': values})
  elif dtype == 'exit':
    values = [ {'x': s.int_session_end, 'y': s.score_bed_exits} for s in sessions]
    return Response({'values': values})
  elif dtype == 'latency':
    values = [ {'x': s.int_session_end, 'y': s.sleep_latency} for s in sessions]
    return Response({'values': values})
  else:
    raise Http404()

