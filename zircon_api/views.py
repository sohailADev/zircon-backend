from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from . import models
from . import serializers
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class SignupViewSet(viewsets.ViewSet):
    serializer_class = serializers.SignupSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            signup_user = models.InstaGramUser.objects.create_user(
                username=serializer.data['username'],
                email=serializer.data['email'],
                password=serializer.data['password'],
                full_name=serializer.data['full_name'],
            )
            if signup_user:
                response = {
                    'success': 'True',
                    'message': 'User registered  successfully',
                    'token': Token.objects.get(user=signup_user).key
                }
                return Response(response, status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)


