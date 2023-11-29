from django.db import models
class Img(models.Model):
    caption = models.CharField(max_length=90)
    filetoupload = models.ImageField(upload_to='image')
    objects=models.Manager
