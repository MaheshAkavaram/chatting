from django.urls import path, include
from rest_framework import routers

from . import admin, views
from .views import ConversationViewSet, MessageViewSet, ReplyViewSet, create_chat_room, redeem_invite_code

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'replies', ReplyViewSet)

urlpatterns = [
    path('conversations', views.ConversationViewSet.as_view({'get': 'list'})),
    path('MessageViewSet', views.MessageViewSet.as_view({'get': 'list'})),
    path('ReplyViewSet', views.ReplyViewSet.as_view({'get': 'list'})),
    path('create_chat_room/', create_chat_room, name="create_chat_room"),
    path('redeem_invite_code/', redeem_invite_code, name="redeem_invite_code"),
    path("invitecode/", views.generate_invite_code, name="generate_invite_code"),

]
