from rest_framework import permissions

from restaurants.models import Restaurant


class IsRestorator(permissions.BasePermission):
    """ Only users who have [is_restaurant_creator=True] can create restaurant """

    def has_permission(self, request, view):
        try:
            return request.user.is_restaurant_creator
        except AttributeError:
            pass





class IsRestaurantCreator(permissions.BasePermission):
    """ Only restaurant creator can create menu of the restaurant """

    def has_permission(self, request, view):
        # Sorry for this stupid part**

        restaurant_id = str(request).split('/')[-3]
        restaurant_creator = Restaurant.objects.get(id=restaurant_id).owner
        return request.user == restaurant_creator


class IsRestaurantCreatorUD(permissions.BasePermission):
    """ Only restaurant creator can update/delete menu of the restaurant """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.restaurant.owner


class MixedPermission:
    """ Permission mixin for action """

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
