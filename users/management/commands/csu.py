import os
import django
from django.core.management.base import BaseCommand
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Создаю пользователя")
        user = User.objects.create(
            email='rastrm@mail.ru',
            first_name='postgree',
            last_name='postgree',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('123')
        print("Создан пользователь")
        user.save()
