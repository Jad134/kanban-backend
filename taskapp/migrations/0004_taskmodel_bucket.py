# Generated by Django 5.0.6 on 2024-07-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_subtaskmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='bucket',
            field=models.CharField(default='todo', max_length=30),
        ),
    ]
