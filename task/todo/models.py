from django.db import models
import datetime
# Create your models here.

class apply(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField(blank=False, auto_now_add=False)
    emailid = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    CreatedOn = models.DateTimeField(default=datetime.datetime.today())
    UpdatedOn = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    objects = models.Manager

    class Meta:
        db_table = 'userregister_table'

class userRegister(models.Model):
    user = models.OneToOneField(apply, related_name='apply', on_delete=models.CASCADE,default=True )
    duration = models.TimeField()
    time = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    objects = models.Manager()

    class Meta:
        db_table = 'apply'