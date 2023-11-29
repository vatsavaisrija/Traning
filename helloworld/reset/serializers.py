from rest_framework import serializers
from .models import resetpassword
class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = resetpassword
        fields = ['name', 'email', 'password', 'confirm_password']

class logserializer(serializers.ModelSerializer):
    class Meta:
        model = resetpassword
        fields = ['email', 'password']

class reseterserializer(serializers.ModelSerializer):
    class Meta:
        model = resetpassword
        fields = ['email', 'password', 'confirm_password']
