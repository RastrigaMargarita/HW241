from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics

from lessons.models import Payment
from lessons.serializers.payment import PaymentSerializer


# 24.2 Настройте фильтрацию для эндпоинтов вывода списка платежей с возможностями:
#  менять порядок сортировки по дате оплаты,
#  фильтровать по курсу или уроку,
#  фильтровать по способу оплаты.

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['kurs', 'type']
    ordering_fields = ['payment_date', '-payment_date', 'amount', '-amount']
