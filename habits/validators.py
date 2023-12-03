from rest_framework.exceptions import ValidationError


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = value.get(self.field)
        if field_value is not None:
            if field_value > 120:
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class RelatedHabitAndRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = value.get(self.field1)
        reward = value.get(self.field2)

        if related_habit and reward:
            raise ValidationError(f"Нельзя одновременно указать {self.field1} и {self.field2}.")


class IsPleasantValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_pleasant = value.get(self.field1)
        related_habit = value.get(self.field2)
        reward = value.get(self.field3)

        if is_pleasant and (related_habit or reward):
            raise ValidationError("Приятная привычка не может иметь связанной привычки или вознаграждения.")


class PeriodValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = value.get(self.field)

        if period is not None:
            if period > 7:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
