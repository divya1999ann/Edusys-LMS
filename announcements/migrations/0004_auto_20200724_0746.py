# Generated by Django 3.0.8 on 2020-07-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_auto_20200724_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/announcements'),
        ),
    ]