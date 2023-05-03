from pay.models import Pay


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


