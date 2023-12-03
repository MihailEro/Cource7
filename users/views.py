from rest_framework import generics

from users.permissions import IsUnauthenticated
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsUnauthenticated]
