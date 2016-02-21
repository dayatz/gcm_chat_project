from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class LoginRequiredMixin(object):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
