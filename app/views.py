import io
import os
import pdb

import PIL.Image as Image
from django.db import models
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, throttle_classes, schema
from rest_framework.generics import (DestroyAPIView, GenericAPIView,
                                     ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.parsers import (FileUploadParser, FormParser, JSONParser,
                                    MultiPartParser)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from .models import ViewTestModel
from .serializers import ViewTestSerializer


class OncePerDayUserThrottle(UserRateThrottle):
        rate = '10/day'


@api_view(['GET', 'POST'])
# @throttle_classes([OncePerDayUserThrottle])
@schema(None)
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


# class TestView(DestroyModelMixin, GenericAPIView):
# class TestView(ListCreateAPIView):
class TestView(RetrieveUpdateDestroyAPIView):
    """
    body - The entire html <body>.
    bodyclass - Class attribute for the <body> tag, empty by default.
    bootstrap_theme - CSS for the Bootstrap theme.
    bootstrap_navbar_variant - CSS class for the navbar.
    branding - Branding section of the navbar, see Bootstrap components.
    breadcrumbs - Links showing resource nesting, allowing the user to go back up the resources.
    It's recommended to preserve these, but they can be overridden using the breadcrumbs block.
    script - JavaScript files for the page.
    style - CSS stylesheets for the page.
    title - Title of the page.

    """
    queryset = ViewTestModel.objects.all()
    serializer_class = ViewTestSerializer


# class ViewTestView(ListModelMixin, GenericAPIView):
#     queryset = TestSerializerModel.objects.all()
#     serializer_class = TestSerializer
#     def get(self, request, *args, **kwargs):
#         print("get method called")
#         return self.list(request, *args, **kwargs)
#
#
# class SnippetList(generics.ListCreateAPIView):
# # class SnippetList(ListModelMixin, GenericAPIView):
#         queryset = TestSerializerModel.objects.all()
#         serializer_class = TestSerializer
#         # renderer_classes = [JSONRenderer]
#         # parser_classes = [JSONParser]
#         # def get(self, request, *args, **kwargs):
#         #     return self.list(request, *args, **kwargs)
#
#
# class TestParserModel(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return self.title
#
# class TestParserModelSerializer(ModelSerializer):
#     class Meta:
#         model = TestParserModel
#         fields = ['title', 'image',]
#
# class TestParser(ListCreateAPIView):
#     queryset = TestParserModel.objects.all()
#     serializer_class = TestParserModelSerializer
