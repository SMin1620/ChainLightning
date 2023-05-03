from django.db import models


# 쿠폰 모델
class Coupon(models.Model):
    name = models.CharField('쿠폰 이름', max_length=45)
    price = models.PositiveIntegerField('무료 쿠폰 금액', default=0)
    created_at = models.DateTimeField('쿠폰 생성', auto_now_add=True)

    class Meta:
        db_table = 'coupon'

    def __str__(self):
        return f'{self.id} : {self.name}, {self.price}'