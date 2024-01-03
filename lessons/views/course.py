from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from lessons.models import Course
from lessons.paginations import PagePagination
from lessons.permissions import IsOwnerOrModerator, IsOwner
from lessons.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = PagePagination
    #permission_classes = [IsOwner]

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = CourseSerializer(paginated_queryset, many=True)
        data_to_return = self.get_paginated_response(serializer.data)
        return data_to_return

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsOwnerOrModerator]
        serializer = CourseSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def newform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get(self):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
