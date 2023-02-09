from django.urls import path, include
from rest_framework import routers

from . import admin, views
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('conversations', views.ConversationViewSet.as_view({'get': 'list'})),
    path('MessageViewSet', views.MessageViewSet.as_view({'get': 'list'})),
]

