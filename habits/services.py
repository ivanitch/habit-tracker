import requests
from django.conf import settings


def send_telegram_message(chat_id: str, message: str):
    """Отправляет сообщение пользователю через Telegram Bot API."""
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()
