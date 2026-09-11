from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import (
    UserProfileSerializer,
    UserRegisterSerializer,
)


class UserCreateAPIView(CreateAPIView):
    """Регистрация нового пользователя (доступна всем)."""
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserProfileAPIView(RetrieveUpdateAPIView):
    """Просмотр и редактирование профиля пользователя."""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Если параметр pk/id не передан в URL,
        автоматически возвращаем профиль текущего авторизованного пользователя.
        """
        if 'pk' not in self.kwargs and 'id' not in self.kwargs:
            return self.request.user
        return super().get_object()
