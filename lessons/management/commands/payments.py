import os
from django.core.management.base import BaseCommand
from datetime import datetime, timezone
from lessons.models import Payment, Course
from users.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment = Payment.objects.create(
            user=User.objects.get(id=1),
            payment_date=datetime.now(tz=timezone.utc),
            course=Course.objects.get(id=1),
            amount=150.45,
            type=Payment.PaymentType.CASH)
        payment.save()
        payment = Payment.objects.create(
            user=User.objects.get(id=1),
            payment_date=datetime.now(tz=timezone.utc),
            course=Course.objects.get(id=2),
            amount=73,
            type=Payment.PaymentType.BANK)
        payment.save()
