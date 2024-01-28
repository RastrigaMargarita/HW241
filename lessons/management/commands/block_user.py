from django.core.management import BaseCommand
from datetime import datetime, timedelta
from django.utils import timezone

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Проверяю пользователей на последний вход в базу")
        current_date = datetime.now(tz=timezone.timezone.utc)
        all_users = User.objects.all()

        for current_user in all_users:
            if current_user.last_login is None:
                current_user.is_active = False
                current_user.save()
            elif current_user.last_login < (current_date - timedelta(days=30)):
                current_user.is_active = False
                current_user.save()
        print("Закончил проверку")