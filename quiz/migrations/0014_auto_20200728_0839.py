# Generated by Django 3.0.8 on 2020-07-28 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20200728_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_answers', to='quiz.temp'),
        ),
    ]
