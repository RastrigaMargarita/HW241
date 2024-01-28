from django.core.mail import send_mail
from django.core.management import BaseCommand
from datetime import datetime, timedelta
from django.utils import timezone
from lessons.models import Subscription, Course
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_date = datetime.now(tz=timezone.timezone.utc)
        curses_to_send = Course.objects.filter(updated__gte=current_date-timedelta(minutes=5))
        print("Начинаю отправку")
        for course_to_send in curses_to_send:

            subscriptions = Subscription.objects.filter(course=course_to_send)

            for subscription in subscriptions:
                user = User.objects.get(id=subscription.user.pk)

                try:
                # Отправка
                    email_to_send = user.email
                    message_to_send = f"Курс {subscription.course} был обновлен, заходите, почитайте."

                    send_mail(
                        "Обновление курса",
                        message_to_send,
                        'RME1C@mail.ru',
                        [email_to_send],
                        fail_silently=False,
                    )

                except Exception as e:
                    print(e)

        print("все отправил")
