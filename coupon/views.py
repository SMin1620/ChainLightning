from django.shortcuts import render
from rest_framework import mixins, viewsets, status

from coupon.models import Coupon
from coupon.serializers import (
    CouponListSerializer,
    UserCouponCreateSerializer,
)


class CouponListViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    쿠폰 조회
    """
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer



