# Generated by Django 3.2.15 on 2022-09-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_remove_restaurant_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]