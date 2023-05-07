from django.db import models

# 결제 방식 클래스
from coupon.models import Coupon
from user.models import User


class Pay(models.Model):
    name = models.CharField('결제 방식', max_length=45)

    class Meta:
        db_table = 'pay'

    def __str__(self):
        return f'{self.id} : {self.name}'


# 결제 히스토리 클래스
class Payment(models.Model):
    cost = models.PositiveIntegerField('결제 지불 금액', default=0)
    charge_cost = models.PositiveIntegerField('선불금 결제 지불 금액', default=0)
    created_at = models.DateTimeField('결제 날짜', auto_now_add=True)

    pay = models.ForeignKey(Pay, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f'{self.id} : user = {self.user.id}, pay = {self.pay.name}'


# 사용자가 결제 수단 선택 후 선불금 충전하는 클래스
class Charge(models.Model):
    created_at = models.DateTimeField('선불금 충전 날짜', auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'id : {self.id} / user : {self.user.username} / coupon : {self.coupon.name}'