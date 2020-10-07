from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class = serializers.LoginSerializer


class SignupViewSet(viewsets.ModelViewSet):
    queryset = models.Signup.objects.all()
    serializer_class = serializers.SignupSerializer