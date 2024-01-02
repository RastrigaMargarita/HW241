from rest_framework import serializers

from lessons.models import Kurs, Lesson
from lessons.serializers.lesson import LessonListSerializer


class KursSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()
    lessons_list = LessonListSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Kurs
        fields = ['id', 'title', 'description', 'picture', 'lessons_count', 'lessons_list']

    def get_lessons_count(self, instance):
        return Lesson.objects.filter(kurs=instance).count()
