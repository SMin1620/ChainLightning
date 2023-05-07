from rest_framework import serializers

from coupon.models import Coupon


class CouponListSerializer(serializers.ModelSerializer):
    """
    쿠폰 리스트
    """
    class Meta:
        model = Coupon
        fields = [
            'id',
            'name',
        ]