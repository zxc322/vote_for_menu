# Generated by Django 3.2.15 on 2022-09-01 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='slug',
        ),
    ]
