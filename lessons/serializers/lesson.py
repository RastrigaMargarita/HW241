from rest_framework import serializers
from lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'title']
