# Generated by Django 3.0.8 on 2020-08-03 14:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200717_1055'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0018_auto_20200731_0809'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='temp',
            new_name='StudentAttemptedList',
        ),
    ]
