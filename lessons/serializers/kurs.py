from rest_framework import serializers

from lessons.models import Kurs, Lesson
from lessons.serializers.lesson import LessonListSerializer


class KursSerializer(serializers.ModelSerializer):
    #24.2 Для модели курса добавьте в сериализатор поле вывода количества уроков.
    #Для сериализатора модели курса реализуйте поле вывода уроков.

    lessons_count = serializers.SerializerMethodField()
    lessons_list = LessonListSerializer(source = "lesson_set", many=True)

    class Meta:
        model = Kurs
        fields = ['id', 'title', 'description', 'picture', 'lessons_count', 'lessons_list']

    def get_lessons_count(self, instance):
        return Lesson.objects.filter(kurs = instance).count()

