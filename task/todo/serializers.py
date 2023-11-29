from rest_framework import serializers
from .models import *

class userregisterserializer(serializers.ModelSerializer):
    class Meta:
        model = apply
        fields = ['fname', 'lname', 'dob', 'emailid', 'address', 'username', 'password']

class someserializer(serializers.ModelSerializer):
    class Meta:
        model = userRegister
        fields = ['user', 'duration']