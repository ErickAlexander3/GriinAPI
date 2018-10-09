from django.contrib.auth.models import User

from rest_framework import serializers, viewsets
from rest_auth.registration.serializers import RegisterSerializer

import pdb

class UserSerializer(serializers.ModelSerializer):
	thrives = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'thrives')


#registration serializer modification
class GriinRegisterSerializer(RegisterSerializer):
	#TODO: find a clean way to display the right field based on some arguemnt (like mode='individual'/'organization')
    phone_number = serializers.CharField()
    #individual info
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    date_of_birth = serializers.DateField()
    #organization info
    organization_name = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(GriinRegisterSerializer, self).__init__(*args, **kwargs)

        mode = self.context.get('request').query_params.get('mode')

        if mode == 'individual':
            for field_name in ['organization_name']:
                self.fields.pop(field_name)

        if mode == 'organization':
            for field_name in ['first_name', 'last_name', 'gender', 'date_of_birth']:
                self.fields.pop(field_name)


    def custom_signup(self, request, user):
    	#TODO: create individual/corporation profile
        pass
