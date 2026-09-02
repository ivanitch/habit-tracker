from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate_duration(self, value):
        if value > 120:
            raise serializers.ValidationError("Время выполнения не может превышать 120 секунд.")
        return value

    def validate_periodicity(self, value):
        if value > 7 or value < 1:
            raise serializers.ValidationError("Привычку нельзя выполнять реже 1 раза в 7 дней.")
        return value

    def validate_linked_habit(self, value):
        if value and not value.is_pleasant:
            raise serializers.ValidationError("Связанная привычка должна быть приятной (is_pleasant=True).")
        return value

    def validate(self, attrs):
        is_pleasant = attrs.get('is_pleasant', False)
        reward = attrs.get('reward')
        linked_habit = attrs.get('linked_habit')

        if reward and linked_habit:
            raise serializers.ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку."
            )

        if is_pleasant and (reward or linked_habit):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )

        return attrs
