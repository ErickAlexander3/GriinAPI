from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Thrive

class ThriveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Thrive
		fields = '__all__'

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
	thrives = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'thrives')

