from rest_framework import serializers
from .models import send


class sendserializer(serializers.ModelSerializer):
    class Meta:
        model = send
        fields = "__all__"