from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from lessons.models import Course
from lessons.paginations import PagePagination
from lessons.permissions import IsOwnerOrModerator, IsOwner, IsNotModerator
from lessons.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    """Курс"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = PagePagination

    def list(self, request, *args, **kwargs):

        self.change_queryset()
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = CourseSerializer(paginated_queryset, many=True)
        data_to_return = self.get_paginated_response(serializer.data)
        return data_to_return

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def change_queryset(self):
        if [IsNotModerator]:
            self.queryset = Course.objects.filter(owner=self.request.user)

    def get_permissions(self):
        print(self.action)
        if self.action == 'create':
            self.permission_classes = [IsNotModerator]
        elif self.action == 'retrive':
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsOwnerOrModerator]
        elif self.action == 'partial_update':
            self.permission_classes = [IsOwnerOrModerator]


        return super(CourseViewSet, self).get_permissions()
