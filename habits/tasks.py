from celery import shared_task
from django.utils import timezone

from .models import Habit
from .services import send_telegram_message


@shared_task
def send_habit_reminders():
    """Проверяет привычки и отправляет уведомления в нужное время."""
    now = timezone.now().time()
    # Ищем привычки, время которых совпадает с текущим (с точностью до минуты)
    # В реальном проекте стоит учитывать дату последнего выполнения, чтобы соблюдать периодичность (periodicity)
    habits = Habit.objects.filter(time__hour=now.hour, time__minute=now.minute)

    for habit in habits:
        # Проверяем, привязан ли у пользователя Telegram ID
        if hasattr(habit.user, 'telegram_chat_id') and habit.user.telegram_chat_id:
            message = f"Напоминание! Пора выполнить привычку:\nЯ буду {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}"
            send_telegram_message(habit.user.telegram_chat_id, message)
