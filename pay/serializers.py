from django.db import transaction
from rest_framework import serializers

from pay.models import Pay, Payment


class UserPaySerializer(serializers.ModelSerializer):
    """
    사용자 결제
    """
    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'pay',
            'order',
            'charge_cost',
            'cost',
        ]

    @transaction.atomic()
    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        payment.charge_cost = payment.user.charge_cost
        payment.cost = payment.order.cost - payment.charge_cost
        payment.user.charge_cost = 0
        payment.status = True
        payment.user.save()
        return payment

