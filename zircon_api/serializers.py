from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
        # fields = ['id','isboast','post_body','post_upvote' ,'post_downvote','date_created','last_update','s_key','total']