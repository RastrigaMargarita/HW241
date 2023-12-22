from django.contrib import admin

from lessons.models import Kurs, Lesson


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'kurs')

