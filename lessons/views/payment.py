import requests
from rest_framework.response import Response
from requests.exceptions import RequestException
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from lessons.models import Payment, PaymentIntens
from lessons.serializers.payment import PaymentSerializer, PaymentIntenseSerializer


class PaymentListView(generics.ListAPIView):
    """Список оплат"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'type']
    permission_classes = [IsAuthenticated]
    ordering_fields = ['payment_date', '-payment_date', 'amount', '-amount']


class PaymentIntenseCreateView(generics.CreateAPIView):
    serializer_class = PaymentIntenseSerializer

    def perform_create(self, serializer):
        print("Оформляю платеж")
        new_payment = serializer.save()

        try:
            url = 'https://api.stripe.com/v1/payment_intents'
            headers = {'Authorization': 'Bearer sk_test_51OVDQQGi3wdveQdkUUTHeqzc49ee6xav0fyrvpyVm4WOsnIdiurJ9tbdYLOWaca31PA0dCSkuKoKV6pRVQVGle6i00pMyMz05S'}
            data = {'amount': '2000', 'currency': 'usd'}

            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()

            # Обработка полученных данных
            new_payment.amount = data['amount']
            new_payment.amount_received = data['amount_received']
            new_payment.payment_id = data['id']

        except RequestException as e:
            # Обработка исключения
            print(e)
            print(Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR))

        new_payment.save()


class PaymentIntenseRetrieveView(generics.UpdateAPIView):
    serializer_class = PaymentIntenseSerializer
    queryset = PaymentIntens.objects.all()

    def perform_update(self, serializer):
        print("Проверяю платеж")

        current_payment = serializer.save()

        try:

            url = f'https://api.stripe.com/v1/payment_intents/{current_payment.payments_id}'

            headers = {
                'Authorization': 'Bearer sk_test_51OVDQQGi3wdveQdkUUTHeqzc49ee6xav0fyrvpyVm4WOsnIdiurJ9tbdYLOWaca31PA0dCSkuKoKV6pRVQVGle6i00pMyMz05S'}

            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()

            # Обработка полученных данных
            current_payment.amount_received = data['amount_received']

        except RequestException as e:
            # Обработка исключения
            print(e)
            print(Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR))

        current_payment.save()
