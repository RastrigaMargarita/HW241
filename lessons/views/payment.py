from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lessons.models import Payment
from lessons.serializers.payment import PaymentSerializer

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'type']
    permission_classes = [IsAuthenticated]
    ordering_fields = ['payment_date', '-payment_date', 'amount', '-amount']
