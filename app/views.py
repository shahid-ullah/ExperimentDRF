from django.shortcuts import render
import os
import io
import pdb
import PIL.Image as Image
from django.db import models

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer

from .models import TestSerializerModel
from .serializers import TestSerializer


class TestListModelMixin(ListModelMixin, GenericAPIView):
    pdb.set_trace()
    queryset = TestSerializerModel.objects.all()
    serializer_class = TestSerializer

class ViewTestView(ListModelMixin, GenericAPIView):
    queryset = TestSerializerModel.objects.all()
    serializer_class = TestSerializer
    def get(self, request, *args, **kwargs):
        print("get method called")
        return self.list(request, *args, **kwargs)


class SnippetList(generics.ListCreateAPIView):
# class SnippetList(ListModelMixin, GenericAPIView):
        queryset = TestSerializerModel.objects.all()
        serializer_class = TestSerializer
        # renderer_classes = [JSONRenderer]
        # parser_classes = [JSONParser]
        # def get(self, request, *args, **kwargs):
        #     return self.list(request, *args, **kwargs)


class TestParserModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class TestParserModelSerializer(ModelSerializer):
    class Meta:
        model = TestParserModel
        fields = ['title', 'image',]

class TestParser(ListCreateAPIView):
    queryset = TestParserModel.objects.all()
    serializer_class = TestParserModelSerializer