from rest_framework import views, response, permissions

from .models import ExtendedUser
from menus.models import Menus


class AddChangeVoteMenuView(views.APIView):
    """ Add vote and change menu votes quantity """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            chosen_menu = Menus.objects.get(id=pk)
        except Menus.DoesNotExist:
            return response.Response(status=404)

        if not request.user.voted_menu:
            ExtendedUser.objects.filter(id=request.user.id).update(voted_menu=pk)
            chosen_menu.votes += 1
            chosen_menu.save()
        else:
            previous_menu = ExtendedUser.objects.get(pk=request.user.id).voted_menu
            previous_menu.votes -= 1
            previous_menu.save()

            ExtendedUser.objects.filter(id=request.user.id).update(voted_menu=pk)
            chosen_menu.votes += 1
            chosen_menu.save()
        return response.Response(status=201)


class PruneView(views.APIView):

    def post(self):
        users = ExtendedUser.objects.all()
        menus = Menus.objects.all()

        for user in users:
            user.voted_menu = None
            user.save()
            print('User PRUNED')

        for menu in menus:
            menu.votes = 0
            menu.save()
            print('Menus PRUNED')

        return response.Response(status=204)
