# Generated by Django 2.0.5 on 2018-12-22 19:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20181222_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='user_id',
            field=models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
