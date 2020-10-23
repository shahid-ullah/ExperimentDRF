# app/serializers.py

from rest_framework import serializers

from .models import TestSerializerModel

# class TestSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSerializerModel
        fields = "__all__"
