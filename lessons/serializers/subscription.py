from rest_framework import serializers
from rest_framework.response import Response

from lessons.models import Subscription, Course


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    label_current_subscriptions = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ["label_current_subscriptions", "label", "course"]

    def get_label_current_subscriptions(self, instance):
        courses = Subscription.objects.filter(user=instance.user).values()
        return "Вы уже подписаны на курсы: " + ", ".join([Course.objects.get(id=course["course_id"]).title for course in courses])

    def get_label(self, instance):
        return "Вы подписываетесь на курс: "


class SubscriptionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "Course"
