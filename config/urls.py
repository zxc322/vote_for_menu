from django.contrib import admin
from django.urls import path, include
from . import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # For old version urls
    path('api/v1/', include(routers)),

    # For latest version
    path('api/v2/', include(routers)),
]
