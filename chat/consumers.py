from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import AsyncToSync

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        AsyncToSync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()
        user = self.scope['user']
        self.send(text_data='Hi %s' % user.username)

    def receive(self, text_data=None, bytes_data=None):
        user = self.scope['user']
        AsyncToSync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },
        )

    def chat_message(self, event):
        self.send(text_data=event["text"])

    def disconnect(self, message):
        AsyncToSync(self.channel_layer.group_discard)("chat", self.channel_name)
