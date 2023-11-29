from django.db import models
# Create your models here.

class Company(models.Model):
    companyname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = models.Manager()

class employ(models.Model):
      user = models.OneToOneField(Company, related_name='Company', on_delete=models.CASCADE,default=True )
      employeeid = models.CharField(max_length=10)
      employeename = models.CharField(max_length=100)
      employeeaddress = models.CharField(max_length=100)
      objects = models.Manager()

class employ1(models.Model):
    user = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    employeename = models.CharField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    objects = models.Manager()