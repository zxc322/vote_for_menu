from django.db import models
from django.contrib.auth.models import AbstractUser
from menus.models import Menus


class ExtendedUser(AbstractUser):
    """ Extend common django user fields"""

    is_employee = models.BooleanField(default=False)
    is_restaurant_creator = models.BooleanField(default=False)

    voted_menu = models.ForeignKey(Menus, on_delete=models.CASCADE, blank=True, null=True)


