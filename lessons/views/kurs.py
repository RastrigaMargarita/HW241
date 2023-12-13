from rest_framework.viewsets import ModelViewSet

from lessons.models import Kurs
from lessons.serializers.kurs import KursSerializer


class KursViewSet(ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
