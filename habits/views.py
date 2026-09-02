from rest_framework import generics

from .serializers import HabitSerializer
from .models import Habit

class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
