from django.db import models

from restaurants.models import Restaurant


class Menus(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True, db_index=True)
    monday = models.TextField(blank=True, null=True)
    tuesday = models.TextField(blank=True, null=True)
    wednesday = models.TextField(blank=True, null=True)
    thursday = models.TextField(blank=True, null=True)
    friday = models.TextField(blank=True, null=True)
    saturday = models.TextField(blank=True, null=True)
    sunday = models.TextField(blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.slug
