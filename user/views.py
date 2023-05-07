from django.shortcuts import render
from rest_framework import mixins, viewsets

from coupon.models import Coupon
from user.models import User
from user.serializers import (
    UserCouponSerializer
)


class UserCouponViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    사용자 쿠폰 발급 뷰셋
    """

    queryset = User.objects.all()
    serializer_class = UserCouponSerializer


