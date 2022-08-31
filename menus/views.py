from django.db.models import Q
from rest_framework import mixins, viewsets, generics, permissions

from .models import Menus
from .serializers import CRUDMenuSerializer, CurrentDayMenusSerializer, WinnersSerializer
from .services import get_current_day_menus_qs
from custom import classes, my_permissions


class CreateMenuAPIView(generics.CreateAPIView):
    """ Create menu """

    queryset = Menus.objects.all()
    serializer_class = CRUDMenuSerializer
    permission_classes = [my_permissions.IsRestaurantCreator]

    def perform_create(self, serializer):
        rest_id = self.kwargs.get('pk')
        print('restik PK:', rest_id)
        serializer.save(restaurant_id=rest_id)


class MenuView(classes.CreateRetrieveUpdateDestroy):
    """ Menu RUD"""
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menus.objects.all().select_related('restaurant')
    serializer_class = CRUDMenuSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [my_permissions.IsRestaurantCreatorUD],
                                    'destroy': [my_permissions.IsRestaurantCreatorUD]}


class TodayMenusAPIView(generics.ListAPIView):
    """ List of menus of current day """

    serializer_class = CurrentDayMenusSerializer

    def get_queryset(self):
        return get_current_day_menus_qs()


class Top5ofTheDayAPIView(generics.ListAPIView):
    """ List of vote winners """

    serializer_class = WinnersSerializer

    def get_queryset(self):
        return Menus.objects.all().order_by('-votes')[:5]
