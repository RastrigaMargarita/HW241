from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lessons.models import Kurs
from lessons.permissions import IsOwnerOrModerator, IsOwner
from lessons.serializers.kurs import KursSerializer


class KursViewSet(ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [IsOwner]

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsOwnerOrModerator]

    def newform_create(self, serializer):
        new_kurs = serializer.save()
        new_kurs.owner = self.request.user
        new_kurs.save()
