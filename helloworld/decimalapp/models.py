from django.db import models

# Create your models here.
class Decimalvalue(models.Model):
    numbers = models.FloatField()
    decimal_field = models.IntegerField()
    converted = models.CharField(max_length=100)
    object = models.Manager
