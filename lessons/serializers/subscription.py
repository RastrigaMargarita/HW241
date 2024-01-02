from rest_framework import serializers
from rest_framework.response import Response

from lessons.models import Subscription, Kurs


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    label_current_subscriptions = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ["label_current_subscriptions", "label", "kurs"]

    def get_label_current_subscriptions(self, instance):
        kurses = Subscription.objects.filter(user=instance.user).values()
        print(kurses)
        return "Вы уже подписаны на курсы: " + \
            ", ".join([Kurs.objects.get(id=kurs["kurs_id"]).title for kurs in kurses])

    def get_label(self):
        return "Вы подписываетесь на курс: "


class SubscriptionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "Kurs"
