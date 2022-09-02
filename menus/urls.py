from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.TodayMenusAPIView.as_view(), name='today'),
    path('get_top/', views.Top5ofTheDayAPIView.as_view(), name='get_top'),
    path('new/', views.CreateMenuAPIView.as_view(), name='create_menu'),
    path('<slug:slug>/', views.MenuView.as_view({
            'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
        })),

]