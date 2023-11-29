from .models import *
from rest_framework import serializers

class teacherserializer(serializers.ModelSerializer):
    class Meta:
          model = teacher
          fields = ['Name','age','number','email', 'password']


class loginserializer(serializers.ModelSerializer):
    class Meta:
          model = teacher
          fields = ["Name",'password']