# app/urls.py

from django.urls import path

from . import api, views

urlpatterns = [
    path('api/users/', api.ListUsers.as_view(), name='user_list'),
    path('', views.hello_world, name='home'),
]
