from django.db import models
class person1(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.IntegerField()
    objects = models.Manager

class person2(models.Model):
    name=models.OneToOneField(person1,related_name="person1", on_delete=models.CASCADE, null=True)
    first_name=models.CharField(max_length=40)
    second_name=models.CharField(max_length=50)
    DOB=models.DateField()
    objects=models.Manager
class person3(models.Model):
    first_name=models.ForeignKey(person1,on_delete=models.CASCADE, null=True)
    ph_no=models.IntegerField()
    password=models.CharField(max_length=60)
    objects=models.Manager


