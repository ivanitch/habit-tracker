from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from .models import Habit


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='12:00:00',
            action='Читать книгу',
            duration=60,
            periodicity=1
        )

    def test_habit_create_duration_validation(self):
        """Тест валидатора: отказ при передаче времени выполнения больше 120 секунд."""
        url = reverse('habits:habits-list')
        data = {
            'place': 'Дом',
            'time': '12:00',
            'action': 'Читать книгу',
            'duration': 150  # Больше 120
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_list(self):
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
