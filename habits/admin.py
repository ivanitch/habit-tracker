from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'action', 'place', 'time', 'is_pleasant', 'linked_habit', 'periodicity', 'reward', 'duration',
        'is_public', 'user')
