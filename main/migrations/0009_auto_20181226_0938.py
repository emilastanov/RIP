# Generated by Django 2.0.5 on 2018-12-26 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20181224_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='term',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 9, 38, 13, 847616), verbose_name='Сделать до'),
        ),
    ]
