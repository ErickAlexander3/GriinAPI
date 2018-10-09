from rest_framework import serializers, viewsets
from .models import Thrive

class ThriveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Thrive
		fields = '__all__'