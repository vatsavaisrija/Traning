# Generated by Django 3.2.20 on 2023-07-22 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_alter_image64_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image64',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 22, 15, 8, 32, 923802)),
        ),
    ]
