from django.contrib import admin

# Register your models here.
from .models import Message, Conversations, Reply, InviteCode, ChatRoom, GroupInviteCode


class Messagesadmin(admin.ModelAdmin):
    list_display = ('conversation', 'text', 'created_at')


admin.site.register(Message, Messagesadmin)


class Conversationsadmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Conversations, Conversationsadmin)


class Replyadmin(admin.ModelAdmin):
    list_display = ('message', 'text', 'created_at')


admin.site.register(Reply, Replyadmin)


class chatadmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_created']


admin.site.register(ChatRoom, chatadmin)


class GroupInviteCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'group')


admin.site.register(GroupInviteCode, GroupInviteCodeAdmin)


class Inviteadmin(admin.ModelAdmin):
    list_display = ('code', 'date_created', 'room')


admin.site.register(InviteCode, Inviteadmin)
