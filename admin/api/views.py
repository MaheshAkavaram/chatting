from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Conversations, InviteCode
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import viewsets
import secrets
from .models import Conversations, Message, Reply, InviteCode
from .serializers import ConversationSerializer, MessageSerializer, ReplySerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversations.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer




def create_chat_room(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    chat_room = Conversations.objects.create(name=name, description=description)
    invite_code = InviteCode.objects.create(room=chat_room)
    return JsonResponse({"invite_code": invite_code.code})



def redeem_invite_code(request):
    code = request.POST.get("code")
    email = request.POST.get("email")
    try:
        validate_email(email)
        invite_code = InviteCode.objects.get(code=code)
        invite_code.redeemed = True
        invite_code.save()
        return JsonResponse({"message": "Successfully joined chat room"})
    except ValidationError:
        return JsonResponse({"message": "Invalid email"})
    except InviteCode.DoesNotExist:
        return JsonResponse({"message": "Invalid invite code"})


from django.shortcuts import render
from .models import GroupInviteCode
from django.http import JsonResponse
import secrets

def generate_invite_code(request):
    code = secrets.token_hex(8)
    invite = GroupInviteCode.objects.create(code=code)
    return JsonResponse({"invite_code": invite.code})
