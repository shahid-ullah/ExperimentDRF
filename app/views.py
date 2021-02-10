# app/views.py
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, schema, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


class ListUsers(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view()
@schema(None)
def hello_world(request):
    return Response({"message": "Hello, world!"})
