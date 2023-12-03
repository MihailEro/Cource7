from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsOwner | IsAdminUser]
    queryset = Habit.objects.all()


class HabitPublicListAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.filter(is_public=True)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]
