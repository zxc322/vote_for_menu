from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from menus.models import Menus
from .models import ExtendedUser
from restaurants.models import Restaurant
from .views import VoteForMenuAPIView


class VoteTest(APITestCase):

    def setUp(self):
        self.user = ExtendedUser.objects.create(username='user1',
                                                password='SomeLongPass',
                                                )

        rest = Restaurant.objects.create(name='REST',
                                         slug='REST',
                                         owner=self.user)

        self.menu1 = Menus.objects.create(restaurant=rest,
                                          name='menu1',
                                          slug='menu1',
                                          monday='some food',
                                          )
        self.menu2 = Menus.objects.create(restaurant=rest,
                                          name='menu2',
                                          slug='menu2',
                                          monday='some food',
                                          )



    def test_vote(self):
        """ Test voting """

        factory = APIRequestFactory()
        user = ExtendedUser.objects.get(username='user1')
        view = VoteForMenuAPIView.as_view()
        request = factory.post(reverse('vote', kwargs={'pk': self.menu1.id}))
        request.user = user
        response = view(request)

        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

