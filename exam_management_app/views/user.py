from rest_framework import viewsets
from exam_management_app.models.user import User
from exam_management_app.serializers.user import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Inherit ReadOnlyModelViewSet
    """
    A viewset that provides only 'retrieve' and 'list' actions for viewing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer