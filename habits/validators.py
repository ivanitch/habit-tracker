from django.core.exceptions import ValidationError


"""
- Исключение одновременного заполнения reward и linked_habit. -> validate(self, attrs)
- duration <= 120 секунд. -> validate_duration(self, value)
- linked_habit обязательно должна иметь is_pleasant=True. -> validate_linked_habit(self, value)
- Если привычка сама is_pleasant=True, у нее не может быть reward или linked_habit. -> validate_is_pleasant(self, value)
- periodicity не более 7 дней. -> validate_periodicity(self, value)
"""
