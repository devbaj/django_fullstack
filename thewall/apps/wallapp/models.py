from django.db import models
from ..login.models import *

# Create your models here.

class MessageManager(models.Manager):
    def add_message(self, userid, postData):
        sender = User.objects.get(id=userid)
        Message.objects.create(sender=sender, message=postData["msg"])
        return True

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="senders")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def add_comment(self, userid, postData):
        user = User.objects.get(id=userid)
        message = Message.objects.get(id=postData["msg-id"])
        Comment.objects.create(message=message, commenter=user, comment=postData["comment"])
        return True

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    commenter = models.ForeignKey(User, related_name="commenters")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()