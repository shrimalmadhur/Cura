from models import *
from serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class SessionViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = SleepSession.objects.all()
  serializer_class = SessionSerializer

  def retrieve(self, request, pk=None):
    session = get_object_or_404(self.queryset, pk=pk)
    ts_data = [ TSDataSerializer(x).data for x in session.time_series_data.all()]

    data = SessionSerializer(session).data
    data['time_series_data'] = ts_data
    return Response(data)
