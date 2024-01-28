from rest_framework import generics

from lessons.models import Lesson
from lessons.paginations import PagePagination
from lessons.permissions import IsOwnerOrModerator, IsOwner, IsNotModerator
from lessons.serializers.lesson import LessonSerializer


class LessonListView(generics.ListAPIView):
    """Список уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = PagePagination

    def get(self, request):
        change_queryset(self)
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonCreateView(generics.CreateAPIView):
    """Добавление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsNotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(generics.UpdateAPIView):
    """Обновление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrModerator]


class LessonRetriveView(generics.RetrieveAPIView):
    """Получение данных урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrModerator]


class LessonDestroyView(generics.DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


def change_queryset(self):
    if [IsNotModerator]:
        self.queryset = Lesson.objects.filter(owner=self.request.user)
