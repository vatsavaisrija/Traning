from rest_framework import serializers
from .models import *
from .estimated import index


class convertserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'age']

    def create(self, validated_data):
        age = validated_data['age']
        print(type(age))
        convert = index(age)
        print(convert)
        user = reversage.objects.create(firstname=validated_data['firstname'],
                                        lastname=validated_data['lastname'],
                                        age=validated_data['age'], dob=convert)
        user.save()
        return user


class dateserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'age', 'dob']

