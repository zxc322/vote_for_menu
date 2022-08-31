from rest_framework import mixins, viewsets

from .my_permissions import MixedPermission


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  MixedPermission,
                                  viewsets.GenericViewSet):
    """
    """
    pass
