from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Conversations(models.Model):
    name = models.CharField(max_length=200)


class Message(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class GroupInviteCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class InviteCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

