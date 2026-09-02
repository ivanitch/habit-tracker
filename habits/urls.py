from django.urls import path

from habits.apps import HabitsConfig

from .views import HabitListView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListView.as_view(), name='habits'),
]
