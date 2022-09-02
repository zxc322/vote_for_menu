from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from restaurants.models import Restaurant


class IsRestorator(permissions.BasePermission):
    """ Only users who have [is_restaurant_creator=True] can create restaurant """

    def has_permission(self, request, view):
        try:
            return request.user.is_restaurant_creator
        except AttributeError:
            pass


class IsEmployee(permissions.BasePermission):
    """ Only users who have [is_employee=True] can vote for menu """

    def has_permission(self, request, view):
        try:
            return request.user.is_employee
        except AttributeError:
            pass


class IsRestaurantCreator(permissions.BasePermission):
    """ Only restaurant creator can create menu of the restaurant """

    def has_permission(self, request, view):
        restaurant_id = request.data.get('restaurant')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        return request.user == restaurant.owner


class IsRestaurantCreatorUD(permissions.BasePermission):
    """ Only restaurant creator can update/delete menu of the restaurant """

    def has_object_permission(self, request, view, obj):
        print('sdadadaddasasd')
        return request.user == obj.restaurant.owner


class MixedPermission:
    """ Permission mixin for action """

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
