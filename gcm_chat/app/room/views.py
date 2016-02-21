from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import ChatRoom
from .serializers import ChatRoomSerializer
from app.core.views import LoginRequiredMixin


class ChatRoomViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['POST'])
    def send_message(self, request, pk):
        self.get_object().send_message(request.data.get('message'))
        return Response({'message': 'sent'}, status=HTTP_200_OK)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            return ChatRoomSerializer(
                remove_fields=['messages'], *args, **kwargs)
        return super(ChatRoomViewSet, self).get_serializer(*args, **kwargs)
