from rest_framework import serializers
from .models import Conversations, Message, Reply


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

