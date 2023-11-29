from django.db import models

class folder(models.Model):
    item_name = models.CharField(max_length=100)
    item_address = models.CharField(max_length=100)
    item_code = models.BinaryField(max_length=150)
    objects = models.Manager

class qrimage(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField()