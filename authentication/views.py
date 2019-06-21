from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

from .serializers import UserSerializer

import json
import requests


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        email = request.data.get('email', '')

        if not username and not password and not email:
            return Response(
                data={
                    "message": "Username, Password and Email are required to create a user"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        new_user = {
            "username": username,
            "password": password,
            "email": email
        }

        serializer = self.serializer_class(data=new_user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Customize token response


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
