# Generated by Django 4.1.10 on 2023-09-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('password', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'Register_table',
            },
        ),
        migrations.CreateModel(
            name='camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('score', models.FloatField()),
                ('user_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='register', to='Backend.register')),
            ],
            options={
                'db_table': 'Campaign_table',
            },
        ),
    ]
