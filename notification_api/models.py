from django.db import models
from InstaGramUser.models import  InstaGramUser
from zircon_api.models import Post


class Notification(models.Model):
    user_to_notify = models.ForeignKey(InstaGramUser, on_delete=models.CASCADE, related_name="user_to_notify")
    post_to_be_notify = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_to_be_notify")
    is_seen = models.BooleanField(default=False)