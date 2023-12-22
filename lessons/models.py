from django.db import models

# Create your models here.
class Kurs(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание", null=True)
    picture = models.ImageField(verbose_name="изображение (превью)", null=True)


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание", null=True)
    picture = models.ImageField(verbose_name="изображение (превью)", null=True)
    video = models.CharField(max_length=500, verbose_name="ссылка на видео", null=True)
    kurs = models.ForeignKey("Kurs", on_delete=models.CASCADE)

# 24.2 Добавьте новую модель «Платежи» со следующими полями:
# пользователь,     дата оплаты,    оплаченный курс или урок,    сумма оплаты,    способ оплаты: наличные или перевод на счет.
# Запишите в эту модель данные через инструмент фикстур или кастомную команду.

class Payment(models.Model):

    class PaymentType(models.TextChoices):
        CASH = '1', 'наличные'
        BANK = '2', 'перевод на банковский счет'

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name="дата платежа")
    kurs = models.ForeignKey("Kurs", verbose_name="курс", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='оплачено', decimal_places=2, max_digits=10)
    type = models.CharField(max_length=1, choices=PaymentType.choices, default=PaymentType.BANK, verbose_name='способ оплаты')



