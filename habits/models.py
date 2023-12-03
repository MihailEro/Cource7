from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=255, verbose_name='место')
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время')
    action = models.CharField(max_length=255, verbose_name='действие')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', blank=True,
                                      null=True)
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    period = models.PositiveSmallIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение')
    duration = models.PositiveIntegerField(default=120, verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
