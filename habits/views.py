from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .serializers import HabitSerializer
from .paginators import HabitPagination
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """
    CRUD для привычек текущего пользователя.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Пользователь видит только свои привычки
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматическая привязка создателя к привычке
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Список публичных привычек.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только публичные привычки
        return Habit.objects.filter(is_public=True)
