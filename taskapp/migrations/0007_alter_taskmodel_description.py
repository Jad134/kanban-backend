# Generated by Django 5.0.6 on 2024-07-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_alter_taskmodel_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
