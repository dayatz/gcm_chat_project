from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from .models import User
from .serializers import UserSerializer
from .functions import send_user_message


class LoginRequiredMixin(object):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['POST'])
    def send_message(self, request, pk):
        message = request.data.get('message')
        send_user_message(pk, message)
