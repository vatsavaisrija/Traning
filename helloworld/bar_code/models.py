from django.db import models

class send(models.Model):
    iteam_name= models.CharField(max_length=200)
    iteam_code= models.IntegerField()
    bar_code = models.BinaryField()
    objects = models.Manager

    class Meta:
        db_table = 'barcode_reader'

# Create your models here.