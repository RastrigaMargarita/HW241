from django.db import models

# Create your models here.
class Kurs(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание")
    picture = models.ImageField(verbose_name="изображение (превью)")

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание")
    picture = models.ImageField(verbose_name="изображение (превью)")
    video = models.CharField(max_length=500, verbose_name="ссылка на видео")