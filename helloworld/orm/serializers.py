from rest_framework import serializers
from .models import Company, employ, employ1


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
         model = Company
         fields = ['companyname', 'username', 'password']


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employ
        fields = ['user', 'employeeid', 'employeename', 'employeeaddress']


class emp1Serializer(serializers.ModelSerializer):

    class Meta:
        model = employ1
        fields = ['user', 'employeename', 'phone', 'password']