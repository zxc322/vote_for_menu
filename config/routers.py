from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="MenuVote API",
      default_version='v2',
      description="Docs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('user_create/', include('users.urls')),
    path('restaurant/', include('restaurants.urls')),
    path('menu/', include('menus.urls')),
]