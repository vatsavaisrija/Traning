# Generated by Django 4.1.10 on 2023-08-03 09:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('emailid', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('CreatedOn', models.DateTimeField(default=datetime.datetime(2023, 8, 3, 14, 42, 59, 463253))),
                ('UpdatedOn', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=20)),
            ],
            options={
                'db_table': 'userregister_table',
            },
        ),
        migrations.CreateModel(
            name='userRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.TimeField()),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 3, 14, 42, 59, 466245))),
                ('user', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='todo.apply')),
            ],
            options={
                'db_table': 'apply',
            },
        ),
    ]
