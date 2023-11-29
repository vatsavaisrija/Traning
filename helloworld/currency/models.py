from django.db import models

# Create your models here.
class numberstowords(models.Model):
    currencys = models.CharField(max_length=100000000)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    objects = models.Manager
    class Meta:
        db_table = 'currency'
