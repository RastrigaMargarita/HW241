import uuid

from django.db import models

from lessons.validators import validate_video_url


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание", null=True)
    picture = models.ImageField(verbose_name="изображение (превью)", null=True)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание", null=True)
    picture = models.ImageField(verbose_name="изображение (превью)", null=True)
    video = models.CharField(max_length=500, verbose_name="ссылка на видео", null=True, validators=[validate_video_url])
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)


class Payment(models.Model):

    class PaymentType(models.TextChoices):
        CASH = '1', 'наличные'
        BANK = '2', 'перевод на банковский счет'

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name="дата платежа")
    course = models.ForeignKey("Course", verbose_name="курс", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='оплачено', decimal_places=2, max_digits=10)
    type = models.CharField(max_length=1, choices=PaymentType.choices, default=PaymentType.BANK,
                            verbose_name='способ оплаты')


class Subscription(models.Model):

    course = models.ForeignKey("Course", null=True, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", null=True, on_delete=models.CASCADE)


class PaymentIntens(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    payments_id = models.CharField(max_length=150, verbose_name='УИ платежа в банке', null=True)
    amount = models.DecimalField(verbose_name='Запрошено', decimal_places=2, max_digits=10, null=True)
    amount_received = models.DecimalField(verbose_name='оплачено', decimal_places=2, max_digits=10, null=True)
