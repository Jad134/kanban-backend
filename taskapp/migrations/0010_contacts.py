# Generated by Django 5.0.6 on 2024-07-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0009_remove_taskmodel_assigned_to_taskmodel_assigned_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]
