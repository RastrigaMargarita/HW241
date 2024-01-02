from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lessons.models import Subscription, Kurs
from lessons.serializers.subscription import SubscriptionCreateSerializer, SubscriptionDeleteSerializer


class SubscribeCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscribe_new = serializer.save()
        subscribe_new.user = self.request.user
        subscribe_new.kurs = Kurs.objects.get(id=self.kwargs['pk'])
        print(self.kwargs['pk'])
        subscribe_new.save()


class SubscribeDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionDeleteSerializer
    permission_classes = [IsAuthenticated]
