from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from lessons.models import Kurs
from lessons.paginations import PagePagination
from lessons.permissions import IsOwnerOrModerator, IsOwner
from lessons.serializers.kurs import KursSerializer


class KursViewSet(ModelViewSet):

    serializer_class = KursSerializer
    queryset = Kurs.objects.all()
    pagination_class = PagePagination
    permission_classes = [IsOwner]

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = KursSerializer(paginated_queryset, many=True)
        data_to_return = self.get_paginated_response(serializer.data)
        return data_to_return

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsOwnerOrModerator]
        serializer = KursSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def newform_create(self, serializer):
        new_kurs = serializer.save()
        new_kurs.owner = self.request.user
        new_kurs.save()

    def get(self):
        queryset = Kurs.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = KursSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
