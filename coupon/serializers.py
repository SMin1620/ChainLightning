from rest_framework import serializers

from coupon.models import Coupon


class UserCouponCreateSerializer(serializers.ModelSerializer):
    """
    사용자 쿠폰 발급
    """
    user = serializers.ReadOnlyField(source='user.User')

    class Meta:
        model = Coupon
        fields = [
            'id',
            'name',
            'user'
        ]


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