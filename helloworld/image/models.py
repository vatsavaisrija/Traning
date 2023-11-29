from django.db import models
import datetime
# Create your models here.

class Image64(models.Model):

   # image_name = models.ImageField(upload_to='image/')
    images=models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    objects = models.Manager()
    class Meta:
       db_table = 'photo'