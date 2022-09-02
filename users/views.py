from rest_framework import mixins, generics, viewsets, permissions

from .models import ExtendedUser
from .serializers import CreateEmployeeSerializer
from . import services


class CreateUserAPIView(generics.CreateAPIView):
    """ Create employee """

    queryset = ExtendedUser.objects.all()
    serializer_class = CreateEmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(is_employee=True)


class CreateRestaurantOwnerAPIView(generics.CreateAPIView):
    """ Create restaurant owner (only these users have permission to upload menus) """

    queryset = ExtendedUser.objects.all()
    serializer_class = CreateEmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(is_restaurant_creator=True)


class VoteForMenuAPIView(services.AddChangeVoteMenuView):
    """ Add vote and change menu votes quantity """
    pass
