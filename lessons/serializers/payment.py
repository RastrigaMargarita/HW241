from rest_framework import serializers
from lessons.models import Payment, PaymentIntens


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentIntenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentIntens
        fields = "__all__"
