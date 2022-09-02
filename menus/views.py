from django.db.models import Q
from rest_framework import mixins, viewsets, generics, permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Menus
from .serializers import CRUDMenuSerializer, CurrentDayMenusSerializer
from .services import get_current_day_menus_qs
from custom import classes, my_permissions


class CreateMenuAPIView(generics.CreateAPIView):
    """ Create menu """

    queryset = Menus.objects.all()
    serializer_class = CRUDMenuSerializer
    permission_classes = [my_permissions.IsRestaurantCreator]



class MenuView(classes.CreateRetrieveUpdateDestroy):
    """ Menu RUD """
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menus.objects.all().select_related('restaurant')
    serializer_class = CRUDMenuSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [my_permissions.IsRestaurantCreatorUD],
                                    'destroy': [my_permissions.IsRestaurantCreatorUD]}

    def create(self, request, *args, **kwargs):
        print('1231231231312')
        print('1231231231312', request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TodayMenusAPIView(generics.ListAPIView):
    """ List of menus of current day """

    serializer_class = CurrentDayMenusSerializer

    def get_queryset(self):
        return get_current_day_menus_qs()


class Top5ofTheDayAPIView(generics.ListAPIView):
    """ List of vote winners """

    serializer_class = CurrentDayMenusSerializer

    def get_queryset(self):
        for el in self.request.headers:
            print(el)
        return Menus.objects.all().order_by('-votes')[:5]
