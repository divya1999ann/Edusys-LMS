# Generated by Django 3.0.8 on 2020-07-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_materials', '0003_auto_20200725_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerial',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/course_materials/'),
        ),
    ]
