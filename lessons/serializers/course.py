from rest_framework import serializers

from lessons.models import Course, Lesson, Subscription
from lessons.serializers.lesson import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()
    lessons_list = LessonListSerializer(source="lesson_set", many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'lessons_count', 'lessons_list', 'is_subscribed']

    def get_lessons_count(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def get_is_subscribed(self, instance):

        if self == {} :
            return Subscription.objects.filter(course=instance, user=self.context.get('request', None).user).exists()
        else:
            return False