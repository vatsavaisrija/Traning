from rest_framework import serializers
from.models import*
class from1serializer(serializers.ModelSerializer):
    class Meta:
        model = person1
        fields = "__all__"
class from2serializer(serializers.ModelSerializer):
    class Meta:
        model = person2
        fields = "__all__"
class from3serializer(serializers.ModelSerializer):
    class Meta:
        model = person3
        fields = "__all__"