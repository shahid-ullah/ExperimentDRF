# app/serializers.py

from rest_framework import serializers

from .models import ViewTestModel

# class TestSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)

class ViewTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewTestModel
        fields = "__all__"
