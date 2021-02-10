# app/api.py
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class ListUsers(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
