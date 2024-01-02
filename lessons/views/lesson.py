from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lessons.models import Lesson
from lessons.paginations import PagePagination
from lessons.permissions import IsOwnerOrModerator, IsOwner
from lessons.serializers.lesson import LessonSerializer


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PagePagination

    def get(self, request):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def newform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


class LessonRetriveView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]
