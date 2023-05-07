from pay.models import Pay, Order


def gen_pay(apps, schema_editor):
    """
    결제 방식 더미데이터
    """

    Pay(
        name='카드'
    ).save()

    Pay(
        name='현금'
    ).save()

    Pay(
        name='카카오페이'
    ).save()

    """
    결제 오더 더미데이터
    """

    Order(
        cost=40000,
        user_id=1,
        pay_id=1
    ).save()
    Order(
        cost=100000,
        user_id=1,
        pay_id=2
    ).save()

