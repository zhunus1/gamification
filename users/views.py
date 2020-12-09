from django.shortcuts import render
import json
from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions, status
from .serializers import UserSerializer,StudentSerializer,StaffSerializer,AuthSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from .authentication import GamificationAuthentication

# Create your views here.

class CreateUserAPIView(APIView):
    # Registration of the platform User
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class CreateStudentAPIView(APIView):
    # Registration of the Student
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class CreateStaffAPIView(APIView):
    # Registration of the Staff
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = StaffSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.get(email=email, password=password)
        if user:
            try:
                token = GamificationAuthentication.get_token_from_credentials(user)
                return Response(token, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)
