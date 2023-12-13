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