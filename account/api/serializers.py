from djoser.serializers import UserCreateSerializer, UserSerializer
from account.models import *
from rest_framework import serializers


class UserCreateSerializer(UserCreateSerializer):
	
	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone']
		extra_kwargs = {
			'password': {
				'write_only': True},
				}
