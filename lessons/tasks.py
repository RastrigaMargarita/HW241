from celery import shared_task
from lessons.management.commands.block_user import Command
from lessons.management.commands.update_mailing import Command as Mailing


@shared_task
def block_users():
    Command.handle(Command())

@shared_task
def update_mailing():
    Mailing.handle(Mailing())
