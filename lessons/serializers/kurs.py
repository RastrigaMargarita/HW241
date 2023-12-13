from rest_framework import serializers

from lessons.models import Kurs


class KursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kurs
        fields = "__all__"
