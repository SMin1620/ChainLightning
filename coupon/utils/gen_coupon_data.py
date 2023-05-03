from coupon.models import Coupon


def gen_coupon(apps, schema_editor):
    Coupon(
        name='가입 축하 쿠폰',
        price=10000
    ).save()

    Coupon(
        name='이벤트 쿠폰',
        price=3000
    ).save()

    Coupon(
        name='데일리 쿠폰',
        price=1000
    ).save()