# Generated by Django 3.1.6 on 2021-02-12 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_auto_20210212_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_all',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Выберите билет'),
        ),
    ]
