from rest_framework import views, response, permissions

from .models import ExtendedUser
from menus.models import Menus
from custom import my_permissions


class AddChangeVoteMenuView(views.APIView):
    """ Add vote and change menu votes quantity """

    permission_classes = [my_permissions.IsEmployee]

    def post(self, request, pk):
        try:
            chosen_menu = Menus.objects.get(id=pk)
        except Menus.DoesNotExist:
            return response.Response(status=404)

        # If user haven't voted yet

        if not request.user.voted_menu:
            print('print only 0')
            ExtendedUser.objects.filter(id=request.user.id).update(voted_menu=pk)
            chosen_menu.votes += 1
            chosen_menu.save()

        # If user have voted for this menu already

        elif request.user.voted_menu.id == pk:
            return response.Response(status=200)

        # If user have voted for another menu already

        else:
            previous_menu = ExtendedUser.objects.get(pk=request.user.id).voted_menu
            previous_menu.votes -= 1
            previous_menu.save()

            ExtendedUser.objects.filter(id=request.user.id).update(voted_menu=pk)
            chosen_menu.votes += 1
            chosen_menu.save()
        return response.Response(status=201)
