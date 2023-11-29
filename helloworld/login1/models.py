from django.db import models


class teacher(models.Model):
    Name = models.CharField(max_length=300)
    age = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        db_table = 'teacher'