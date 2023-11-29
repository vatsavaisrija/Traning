from django.db import models


# Create your models here.
class resetpassword(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    objects = models.Manager
