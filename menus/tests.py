import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Menus
from restaurants.models import Restaurant
from users.models import ExtendedUser
from .services import get_current_day_as_str


class GetTopMenusTests(APITestCase):

    def setUp(self):
        user = ExtendedUser.objects.create(username='user1',
                                           password='SomeLongPass',
                                           )

        rest = Restaurant.objects.create(name='REST',
                                         slug='REST',
                                         owner=user)
        name = 'test_'
        for i in range(10):
            self.menu = Menus.objects.create(restaurant=rest,
                                             name=name + str(i),
                                             slug=name + str(i),
                                             monday='some food',
                                             tuesday='some food',
                                             wednesday='some food',
                                             thursday='some food',
                                             friday='some food',
                                             saturday='some food',
                                             sunday='some food',
                                             votes=random.randint(0, 19))
            i += 1

    def test_top(self):
        """ Test top voted menus list (top1 with idx 0, top2 with idx 1 and so on """

        response = self.client.get(reverse('get_top'))
        assert response.json()[0]['votes'] >= response.json()[2]['votes'] >= response.json()[4]['votes']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_current_day(self):
        """ Test top voted menus list (top1 with idx 0, top2 with idx 1 and so on """

        response = self.client.get(reverse('today'))
        print(response.headers)
        today = get_current_day_as_str()
        for menu in response.json():
            day_menu = list(menu.keys())[-1]
            print(today, '=>', day_menu)
            self.assertEqual(day_menu, today)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
