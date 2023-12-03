from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test user",
            password="12345",
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="Дом",
            time="7:15:00",
            action="Зарядка",
            reward="Фреш",
            user=self.user,
        )

    def test_get_habits(self):
        url = reverse("habits:habits-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response.json(),
                         {
                             "count": 1,
                             "next": None,
                             "previous": None,
                             "results": [
                                 {
                                     "id": self.habit.id,
                                     "place": self.habit.place,
                                     "time": self.habit.time,
                                     "action": self.habit.action,
                                     "is_pleasant": self.habit.is_pleasant,
                                     "period": self.habit.period,
                                     "reward": self.habit.reward,
                                     "duration": self.habit.duration,
                                     "is_public": self.habit.is_public,
                                     "user": self.habit.user_id,
                                     "related_habit": self.habit.related_habit
                                 }
                             ]
                         }
                         )

    def test_get_public_habits(self):
        url = reverse("habits:habits-public-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habits(self):
        url = reverse("habits:habits-create")
        data = {
            "place": "Офис",
            "time": "13:00:00",
            "action": "Выполнить задачи",
            "reward": "кофе",
            "is_public": True,
            "user": self.habit.user_id,
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_update_habits(self):
        url = reverse("habits:habits-update", args=[self.habit.id])
        data = {
            "place": "Улица",
            "time": "19:30:00",
            "action": "Пробежка",
            "reward": "Кино",
            "is_public": True,
            "user": self.habit.user_id,
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habits(self):
        url = reverse("habits:habits-delete", args=[self.habit.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_duration_validator(self):
        url = reverse("habits:habits-create")
        data = {
            "place": "Дом",
            "time": "21:00:00",
            "action": "Приготовить ужин",
            "reward": "Печенька",
            "is_public": True,
            "user": self.habit.user_id,
            "duration": 121
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)

    def test_period_validator(self):
        url = reverse("habits:habits-create")
        data = {
            "place": "Дом",
            "time": "7:00:00",
            "action": "Душ",
            "reward": "Фреш",
            "is_public": True,
            "user": self.habit.user_id,
            "period": 11
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)

    def test_is_pleasant_validator(self):
        url = reverse("habits:habits-create")
        data = {
            "place": "Улица",
            "time": "19:00:00",
            "action": "Пробежка",
            "reward": "Фаст Фуд",
            "is_pleasant": True,
            "is_public": True,
            "user": self.habit.user_id
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)
