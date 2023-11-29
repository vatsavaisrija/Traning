from rest_framework import serializers
from .models import *
from .measure import calculateage


class converterserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'dob']

    def create(self, validated_data):
        dob = validated_data['dob']
        print(type(dob))
        convert =calculateage(dob)
        print(convert)
        user = reversage.objects.create(firstname=validated_data['firstname'],lastname=validated_data['lastname'],
                                        dob=validated_data['dob'], age=convert)
        user.save()
        return user


class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'dob']

class ageserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname','dob','age']