# Generated by Django 3.2.20 on 2023-07-29 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0019_alter_image64_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image64',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 29, 11, 11, 31, 161960)),
        ),
    ]
