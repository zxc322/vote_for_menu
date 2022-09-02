from rest_framework import serializers

from .models import Menus
from .services import get_current_day_as_str


class CRUDMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus

        exclude = ['votes']


class CurrentDayMenusSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Menus

        fields = ['id', 'restaurant', 'name', 'slug', 'votes', get_current_day_as_str()]


