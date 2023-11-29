from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    objects = models.Manager
    class Meta :
        db_table = 'employees'