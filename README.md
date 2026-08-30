# Habit Tracker — трекер привычек

Бэкенд-часть трекера привычек, разработанная на базе **Django 6** и **Django REST Framework (DRF)**.

---

## Стек технологий

* **Python:** 3.12+
* **Фреймворк:** Django 6.1
* **API:** Django REST Framework (DRF)
* **База данных:** PostgreSQL
* **Менеджер пакетов и окружений:** `uv`

---

## Функционал

---

## Основные эндпоинты API

---

## Установка и запуск

1. **Клонирование репозитория:**

```bash
git clone git@github.com:ivanitch/habit-tracker.git habit-tracker
cd habit-tracker
```

2. **Настройка окружения:**

```bsah
cp .env.example .env
uv sync
```

3. **Миграции:**

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

4. **Загрузка тестовых данных и фикстуры групп:**


5. **Создание суперпользователя:**

```bash
uv run python manage.py createsuperuser
```

6. **Запуск сервера**

```bash
uv run python manage.py runserver

# или
./server.sh
```

7. **Тестирование и покрытие кодом**

```bash
uv run python manage.py test

uv run coverage run --source='.' manage.py test
uv run coverage report
```
