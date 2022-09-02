from celery import shared_task

from users.models import ExtendedUser
from .models import Menus


@shared_task
def pruner():
    users = ExtendedUser.objects.all()
    menus = Menus.objects.all()

    for user in users:
        user.voted_menu = None
        user.save()
        print('Users with ID "{}" - voted field have been PRUNED'.format(user.id))

    for menu in menus:
        menu.votes = 0
        menu.save()
        print('Menu with id "{}" - votes have been PRUNED'.format(menu.id))
