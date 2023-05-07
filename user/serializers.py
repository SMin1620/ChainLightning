from rest_framework import serializers
from django.db import transaction

from coupon.models import Coupon
from pay.models import Charge


class UserCouponSerializer(serializers.ModelSerializer):
    """
    사용자 쿠폰 발급 시리얼라이저
    """

    class Meta:
        model = Charge
        fields = [
            'user',
            'coupon',
            'created_at'
        ]

    @transaction.atomic()
    def create(self, validated_data):
        charge = Charge.objects.create(**validated_data)
        charge.user.charge_cost += charge.coupon.price
        charge.user.save()
        return charge


