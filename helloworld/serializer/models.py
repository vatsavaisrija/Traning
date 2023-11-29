from django.db import models


# Create your models here.


class buyer(models.Model):
    ticketclass = models.CharField(max_length=200)
    movie_name = models.CharField(max_length=200)
    theatre = models.CharField(max_length=200)
    seat_no = models.CharField(max_length=200)

    objects = models.Manager()

    class Meta:
        db_table = 'buyer'


