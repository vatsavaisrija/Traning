from rest_framework import serializers
from .models import numberstowords
class DatetimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = numberstowords
        fields = ['amount']
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = numberstowords
        fields = '__all__'