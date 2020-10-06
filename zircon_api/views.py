from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer