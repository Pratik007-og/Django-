from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    numberofviews = models.IntegerField()
    numberoflikes = models.IntegerField()
    class Meta:
        db_table = "q1_category"

class Page(models.Model):
    category = models.CharField(max_length = 100)
    title = models.CharField(max_length=100)
    url = models.URLField()
    views = models.IntegerField()
    class Meta:
        db_table = "q1_page"