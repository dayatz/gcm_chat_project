from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message


class ChatRoomSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ChatRoomSerializer, self).__init__(*args, **kwargs)
        if remove_fields:
            for field in remove_fields:
                self.fields.pop(field)

    messages = MessageSerializer(required=False)

    class Meta:
        model = ChatRoom