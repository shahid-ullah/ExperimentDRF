# app/serializers.py

from rest_framework import serializers

from .models import Post, ViewTestModel


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Post
        fields = ['title', 'body']
        # fields = "__all__"


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        # breakpoint()
        return 'custom value from create watchdog'

    def update(self, instance, validated_data):
        return 'custom value from update'
        # breakpoint()


class ViewTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewTestModel
        fields = "__all__"
