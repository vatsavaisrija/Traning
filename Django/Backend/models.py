from django.db import models

class register(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.TextField()
    address = models.TextField()
    objects = models.Manager()

    class Meta:
        db_table ='Register_table'

class camp(models.Model):
    # STATUS_CHOICES = (
    #     ("JAVA",'java'),
    #     ('PYTHON','python'),
    #     ("CSS",'css'),
    #     ("HTML", 'html'),)
    # STREAM_CHOICES = (
    #     ("CSE",'cse'),
    #     ("ECE",'ece'),
    #     ("MECH",'mech'),
    #     ("CIVIL",'civil'),
    #     ("EEE",'eee'),
    # )
    #YEAR_CHOICES = [(year, year) for year in range(2017, 2024)]
    #SCORE_CHOICES = [(score, score) for score in range(1, 11)]
    user_details = models.OneToOneField(register, related_name="register", on_delete=models.CASCADE,default=True, null=True)
    skills = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    year = models.IntegerField()
    score = models.FloatField()
    objects = models.Manager()

    def name(self):
        return self.user_details.name


    class Meta:
        db_table = 'Campaign_table'