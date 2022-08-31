from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.CreateRestaurantAPIView.as_view(), name='create_restaurant'),
]
