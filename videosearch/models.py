from django.db import models
from django.utils.timezone import now


class Video(models.Model):
    videoId = models.CharField(max_length=100, verbose_name="id")
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    publishedAt = models.DateTimeField(verbose_name='Опубликовано', default=now)
    channelTitle = models.CharField(max_length=100, verbose_name='Название канала')
    thumbnail = models.URLField(verbose_name='Превью')
    views = models.IntegerField(verbose_name='Просмотры')

    class Meta:
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'
