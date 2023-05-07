from django.shortcuts import render
from rest_framework import mixins, viewsets, status

from coupon.models import Coupon
from coupon.serializers import (
    CouponListSerializer,
)


class CouponListViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    쿠폰 조회
    """
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer



