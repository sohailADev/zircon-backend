from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from . import models
from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that fetches all posts
    """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.InstaGramUser.objects.all()
    serializer_class = serializers.LoginSerializer


class SignupViewSet(viewsets.ModelViewSet):
    queryset = models.InstaGramUser.objects.all()
    serializer_class = serializers.SignupSerializer
