from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitPublicListAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('', HabitListAPIView().as_view(), name='habits-list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habits-public-list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]
