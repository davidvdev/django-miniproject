from django.db import models

# Create your models here.
class Map(models.Model):
    rows = models.IntegerField()
    columns = models.IntegerField()
    layout = models.CharField(max_length=100)