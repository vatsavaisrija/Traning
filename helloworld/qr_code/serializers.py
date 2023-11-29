from rest_framework import serializers
from .models import folder


class folderSerializer(serializers.ModelSerializer):
    class Meta:
        model = folder
        fields = "__all__"