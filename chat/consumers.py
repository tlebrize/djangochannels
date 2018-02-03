from channels.generic.websocket import JsonWebsocketConsumer

class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.username = 'Anonymous'
        self.accept()
        self.send_json(content='Hi %s' % self.username)

    def receive_json(self, content):
        text = content['msg']
        if text.startswith("/name"):
            self.username = text[5:].strip()
            self.send_json(content="[set your username to %s]" % self.username)
        else:
            self.send_json(content=self.username + ": " + text)

    def disconnect(self, message):
        pass