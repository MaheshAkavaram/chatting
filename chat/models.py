from django.db import models


# Create your models here.

class Conversation(models.Model):
    name = models.CharField(max_length=200)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


