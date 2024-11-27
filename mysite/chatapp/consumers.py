from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom,ChatMessage
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f"chat_{self.room_name}"
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @sync_to_async
    def get_user_id(self, username):
        try:
            user = User.objects.get(username=username)
            return user.id
        except User.DoesNotExist:
            return None

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)  # Ensure `text_data` is used if provided
        message = data['message']
        username = data['username']
        room = data['room']

        # Get user ID from the database (sync_to_async is used to avoid blocking)
        user_id = await self.get_user_id(username)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'user_id': user_id,  # Pass user ID
                'room': room,
            }
        )

        await self.save_message(username, room, message)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        user_id = event['user_id']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'user_id': user_id,
            'room': room,
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        try:
            user = User.objects.get(username=username)
            room = ChatRoom.objects.get(slug=room)
            ChatMessage.objects.create(user=user, room=room, message_content=message)
        except (User.DoesNotExist, ChatRoom.DoesNotExist):
            # Log the error or handle it
            pass

    