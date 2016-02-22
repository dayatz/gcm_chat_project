from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from app.core.views import LoginRequiredMixin


class ChatRoomViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['POST'])
    def send_message(self, request, pk):
        message = request.data.get('message')
        m = Message.objects.create(
            user=request.user, room_id=pk, message=message)
        self.get_object().send_message(message)
        serializer = MessageSerializer(m)
        return Response(serializer.data, status=HTTP_200_OK)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            return ChatRoomSerializer(
                remove_fields=['messages'], *args, **kwargs)
        return super(ChatRoomViewSet, self).get_serializer(*args, **kwargs)
