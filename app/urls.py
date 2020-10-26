# app/urls.py

from django.urls import path

from . import views
# from .views import SnippetList, TestParser, TestView

urlpatterns = [
    path('<int:pk>/', views.TestView.as_view(), name='home'),
    # path('', ViewTestView.as_view(), name='home'),
    # path('', SnippetList.as_view(), name='home'),
    # path('api/', TestParser.as_view(), name='api'),
]
