from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
        # fields = ['id','isboast','post_body','post_upvote' ,'post_downvote','date_created','last_update','s_key','total']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstaGramUser
        fields = ['username', 'password', 'email', 'full_name']
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #         'style': {'input_type': 'password'}
        #     }
        # }
