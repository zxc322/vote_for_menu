from .models import ExtendedUser


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



