from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class InstaGramUser(AbstractUser):
    full_name = models.CharField(max_length=80)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank=True, null=True)
    GENDER_CHOICES = [('Male','Male'),('Female', 'Female'),('Custom', 'Custom'),('Prefer Not To Say', 'Prefer Not To Say')]
    gender = models.CharField(max_length=20, default='Prefer Not To Say', choices=GENDER_CHOICES)
    email = models.EmailField(max_length=254)
    # REQUIRED_FIELDS = ['full_name',]

    def __str__(self):
        return self.full_name

class Post(models.Model):
    caption = models.CharField(max_length=280)
    image = models.ImageField(upload_to='user_upload/')
    # likes = models.
    # comment = 
    # location = models.URLField()
    author = models.ForeignKey(InstaGramUser, on_delete=models.CASCADE, related_name="author")
    create_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.caption

class Notification(models.Model):
    user_to_notify = models.ForeignKey(InstaGramUser, on_delete=models.CASCADE, related_name="user_to_notify")
    post_to_be_notify = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_to_be_notify")
    is_seen = models.BooleanField(default=False)

    
    

