# app/urls.py

from django.urls import path

from .views import SnippetList, TestParser, ViewTestView
from . import views

urlpatterns = [
    path('', views.TestListModelMixin.as_view(), name='home'),
    # path('', ViewTestView.as_view(), name='home'),
    # path('', SnippetList.as_view(), name='home'),
    path('api/', TestParser.as_view(), name='api'),
]
