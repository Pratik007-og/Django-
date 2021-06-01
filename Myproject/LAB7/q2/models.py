from django.db import models

# Create your models here.
class works(models.Model):
    pname = models.CharField(max_length = 100)
    cname = models.CharField(max_length = 100)
    salary = models.IntegerField()

    class Meta:
        db_table = "works"

class lives(models.Model):
    pname = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)

    class Meta:
        db_table = "lives"