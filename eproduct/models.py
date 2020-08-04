from django.db import models


class Item(models.Model):
    fruit_name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=3025)

