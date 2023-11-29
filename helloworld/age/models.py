from django.db import models

class reversage(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    objects = models.Manager


    class Meta:
        db_table = "age"






#agebased on the calculate another task
