from rest_framework import mixins, viewsets

from pay.models import Payment
from pay.serializers import (
    UserPaySerializer
)


class UserPayViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    사용자 충전 결제 뷰셋
    """
    model = Payment
    serializer_class = UserPaySerializer
