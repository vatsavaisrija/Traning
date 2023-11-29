from django.db import models

# Create your models here.
class employe(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    objects = models.Manager

    class Meta:
        db_table = 'employee'