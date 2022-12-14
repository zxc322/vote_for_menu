from django.urls import path, include
from . import views, services

urlpatterns = [
    path('employee/', views.CreateUserAPIView.as_view(), name='create_employee'),
    path('restaurant_owner/', views.CreateRestaurantOwnerAPIView.as_view(), name='create_RO'),
    path('vote/<int:pk>/', services.AddChangeVoteMenuView.as_view(), name='vote'),
]
