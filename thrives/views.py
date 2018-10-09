from django.shortcuts import render
from rest_framework import viewsets

from django.contrib.auth.models import User
from .models import Thrive
from .serializers import ThriveSerializer
from griin_auth.serializers import UserSerializer

# Viewsets
class ThriveViewSet(viewsets.ModelViewSet):
	queryset = Thrive.objects.all()
	serializer_class = ThriveSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
