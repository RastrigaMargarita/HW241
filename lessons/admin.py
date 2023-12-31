from django.contrib import admin

from lessons.models import Course, Lesson, Subscription, PaymentIntens


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course')


@admin.register(PaymentIntens)
class PaymentIntens(admin.ModelAdmin):
    list_display = ('amount', 'amount_received')
