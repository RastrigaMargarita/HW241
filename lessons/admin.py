from django.contrib import admin

from lessons.models import Kurs, Lesson, Subscription


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'kurs')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'kurs')
