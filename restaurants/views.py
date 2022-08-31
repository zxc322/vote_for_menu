from rest_framework import mixins, viewsets, generics, response

from .models import Restaurant
from .serializers import CreateRestaurantSerializer
from custom.my_permissions import IsRestorator


class CreateRestaurantAPIView(generics.CreateAPIView):

    queryset = Restaurant.objects.all()
    serializer_class = CreateRestaurantSerializer
    permission_classes = [IsRestorator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



