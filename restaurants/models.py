from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    #  set owner to give him permission for menu upload

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owner')

    def __str__(self):
        return self.name
