from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        extra_kwargs = {
            'message': {'required': False},
            'room': {'required': False, 'write_only': True},
            'user': {'required': False}
        }


class ChatRoomSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ChatRoomSerializer, self).__init__(*args, **kwargs)
        if remove_fields:
            for field in remove_fields:
                self.fields.pop(field)

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        extra_kwargs = {
            'user': {'required': False},
            'description': {'required': False}
        }
