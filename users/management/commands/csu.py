import os
import django
from django.core.management.base import BaseCommand
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from users.models import User


class Command(BaseCommand):

    #def handle(self, *args, **options):
    #    print("Создаю пользователя")
    #    user = User.objects.create(
    #        email='rastrm@mail.ru',
    #        first_name='postgree',
    #        last_name='postgree',
    #        is_superuser=True,
    #        is_staff=True,
    #        is_active=True
    #    )
    #    user.set_password('123')
    #    print("Создан пользователь")
    #    user.save()
    def handle(self, *args, **options):
        print("Создаю пользователя Alien")
        user = User.objects.create(
            email='alien@mail.ru',
            first_name='alien',
            last_name='alien',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )
        user.set_password('123')
        print("Создан пользователь")
        user.save()
