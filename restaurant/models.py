from django.db import models
from django.contrib.postgres.fields import ArrayField


class FoodDetail(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    available_timing = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    order_id = models.CharField(max_length=100, primary_key=True, unique=True)
    restaurant_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ordered_items = models.CharField(max_length=255)   
    bill_amount = models.IntegerField()
    order_timestamp = models.DateTimeField()


    def __str__(self):
        return self.restaurant_name
