# Generated by Django 3.2.20 on 2023-07-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=90)),
                ('filetoupload', models.ImageField(upload_to='image')),
            ],
        ),
    ]
