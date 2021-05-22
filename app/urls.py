# app/urls.py

from django.urls import path

from . import api, views

urlpatterns = [
    path('api/users/', api.ListUsers.as_view(), name='user_list'),
    path('new/', views.post_new_view, name='post_new'),
    # path('', views.hello_world, name='home'),
]
