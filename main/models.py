from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date,datetime


class Tasks(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Адрес')
    user = models.ForeignKey(User,
                                 related_name='user_created',
                                 on_delete=models.CASCADE,
                                 verbose_name='Создатель задания')
    created = models.DateField(verbose_name='Создано', default=date.today)
    term = models.DateTimeField(verbose_name='Сделать до', default=datetime.now())

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse("main:task_detail",
                       args=[self.id, self.slug])

    def __str__(self):
        return "Задание: {0} ({1})".format(self.title, self.user)

class Events(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateField(auto_now=True, verbose_name='Создано')
    term = models.DateTimeField(verbose_name='Сделать до')
    status = models.BooleanField(verbose_name='Статус', default=False)

    event = models.ForeignKey(
        Tasks,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Событие'
    )


    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return "Событие: {0}".format(self.title)