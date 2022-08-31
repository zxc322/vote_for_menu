from rest_framework import serializers

from .models import Menus
from .services import get_current_day_as_str


class CRUDMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menus

        exclude = ['restaurant']


class CurrentDayMenusSerializer(serializers.ModelSerializer):

    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Menus

        fields = ['restaurant', 'name', get_current_day_as_str()]


class WinnersSerializer(serializers.ModelSerializer):

    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Menus

        fields = ['restaurant', 'name', 'votes', get_current_day_as_str()]
