from rest_framework import serializers
from .models import buyer

class buyerserializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = ['ticketclass','movie_name','theatre','seat_no']



class resetserializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = ['ticketclass','movie_name','theatre','seat_no']