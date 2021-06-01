from django.db import models

# Create your models here.
class author(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    email = models.EmailField()
    class Meta:
        db_table = "author"

class publisher(models.Model):
    name = models.CharField(max_length = 100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()
    class Meta:
        db_table = "publisher"

class book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    class Meta:
        db_table = "book"