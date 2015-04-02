from rest_framework import viewsets
from django.contrib.auth.models import User
from serializers import *

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
