# Generated by Django 5.0 on 2024-01-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_rename_payment_id_paymentintens_payments_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(null=True, verbose_name='дата последнего апдейта'),
        ),
    ]
