from rest_framework import serializers
from .models import *

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields ="__all__"

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ["email","password"]

class forgetserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields =["email","password"]

class campserializer(serializers.ModelSerializer):
    class Meta:
        model = camp
        fields = "__all__"

class skillserializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name', read_only=True)
    class Meta:
        model = camp
        fields = ["skills","user_details","name"]


class streamserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    class Meta:
        model = camp
        fields = ["stream","user_details","name"]

class yearserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    class Meta:
        model = camp
        fields = ["year","user_details","name"]

class scoreserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    class Meta:
        model = camp
        fields = ["score","user_details","name"]