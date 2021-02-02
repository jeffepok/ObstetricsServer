from djoser.serializers import UserCreateSerializer, UserSerializer
from account.models import *
from rest_framework import serializers


class UserCreateSerializer(UserCreateSerializer):
	
	class Meta:
		model = Account
		fields = ['email', 'password', 're_password']
		extra_kwargs = {
			'password': {
				'write_only': True},
				}
