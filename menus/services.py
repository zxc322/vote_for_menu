import datetime

from .models import Menus


def get_current_day_idx():
    day_index = datetime.datetime.today().weekday()
    return day_index


def get_current_day_menus_qs():
    day_index = get_current_day_idx()
    if day_index == 0:
        return Menus.objects.exclude(monday__isnull=True).exclude(monday__exact='').select_related('restaurant')
    elif day_index == 1:
        return Menus.objects.exclude(tuesday__isnull=True).exclude(tuesday__exact='').select_related('restaurant')
    elif day_index == 2:
        return Menus.objects.exclude(wednesday__isnull=True).exclude(wednesday__exact='').select_related('restaurant')
    elif day_index == 3:
        return Menus.objects.exclude(thursday__isnull=True).exclude(thursday__exact='').select_related('restaurant')
    elif day_index == 4:
        return Menus.objects.exclude(friday__isnull=True).exclude(friday__exact='').select_related('restaurant')
    elif day_index == 5:
        return Menus.objects.exclude(saturday__isnull=True).exclude(saturday__exact='').select_related('restaurant')
    elif day_index == 6:
        return Menus.objects.exclude(sunday__isnull=True).exclude(sunday__exact='').select_related('restaurant')


def get_current_day_as_str():
    day_index = get_current_day_idx()
    if day_index == 0:
        return 'monday'
    elif day_index == 1:
        return 'tuesday'
    elif day_index == 2:
        return 'wednesday'
    elif day_index == 3:
        return 'thursday'
    elif day_index == 4:
        return 'friday'
    elif day_index == 5:
        return 'saturday'
    elif day_index == 6:
        return 'sunday'
